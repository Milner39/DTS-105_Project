from typing import Unpack
import customtkinter as ctk
from .FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes
from ..theme import Colors, Sizes



class ScrollableComponent(FragmentComponent):
  """
  | A scrollable frame.
  |
  | Defaults to a transparent background (like `FragmentComponent`) so it can
    sit on any surface without painting over it. The scrollbar is auto-hidden
    when content fits in the visible area.
  |
  | Add content by using `scrollable.content` as the master.
  """

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    **kwargs: Unpack[GuiTypes.CTkFrameKwargsT]
  ):
    if "fg_color" not in kwargs: kwargs.update(fg_color="transparent")

    super().__init__(master, **kwargs)

    self.SCROLL_WRAPPER_PADDING:  int = Sizes.Spacing.sm
    self.CONTENT_PADDING:         int = Sizes.Spacing.md


    # Inset this frame so master's borders are visible if set
    master_border_width = self.master.cget("border_width")
    self.pack(fill="both", expand=True,
      padx=master_border_width, pady=master_border_width
    )

    # The frame with the scroll bar
    scroll_wrapper = ctk.CTkScrollableFrame(self,
      fg_color="transparent",
      corner_radius=0,
      scrollbar_fg_color="transparent",
      scrollbar_button_color=Colors.Surface.border,
      scrollbar_button_hover_color=Colors.Grayscale.neutral_500
    )
    scroll_wrapper.pack(fill="both", expand=True,
      padx=self.SCROLL_WRAPPER_PADDING, pady=self.SCROLL_WRAPPER_PADDING
    )
    self._scroll_wrapper = scroll_wrapper


    # The content to scroll
    content = FragmentComponent(scroll_wrapper)
    content.pack(fill="x",
      padx=self.CONTENT_PADDING, pady=self.CONTENT_PADDING
    )
    self.content = content


    # Fires when the content size changes.
    self.content.bind("<Configure>",
      self._update_scrollbar_visibility, add=True
    )

    # Fires when this component resizes.
    self._scroll_wrapper._parent_canvas.bind("<Configure>",
      self._update_scrollbar_visibility, add=True
    )



  @property
  def natural_height(self) -> int:
    """Height needed to show all content without scrolling."""
    return sum([
      (2 * self.SCROLL_WRAPPER_PADDING),
      (2 * self.CONTENT_PADDING),
      self.content.winfo_reqheight()
    ])

  @property
  def natural_bordered_height(self) -> int:
    """Height needed to show all content without scrolling, including border width."""
    return sum([
      (2 * self.master.cget("border_width")),
      self.natural_height
    ])


  def _update_scrollbar_visibility(self, _event=None) -> None:
    height = self.winfo_height()
    should_show = height < self.natural_height
    is_shown = bool(self._scroll_wrapper._scrollbar.winfo_ismapped())

    if should_show and not is_shown:
      # Not enough room for content, show scroll bar
      self._scroll_wrapper._scrollbar.grid()

    elif not should_show and is_shown:
      # Is enough room for content, hide scroll bar
      self._scroll_wrapper._scrollbar.grid_remove()

from typing import Unpack
import customtkinter as ctk
from .. import type_defs as GuiTypes
from ..theme import Colors



class ScrollableComponent(ctk.CTkScrollableFrame):
  """
  | A scrollable frame.
  |
  | Defaults to a transparent background (like `FragmentComponent`) so it can
    sit on any surface without painting over it. The scrollbar is auto-hidden
    when content fits in the visible area.
  """

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    **kwargs: Unpack[GuiTypes.CTkFrameKwargsT]
  ):
    if "fg_color" not in kwargs: kwargs.update(fg_color="transparent")

    super().__init__(
      master,
      scrollbar_fg_color="transparent",
      scrollbar_button_color=Colors.Surface.border,
      scrollbar_button_hover_color=Colors.Grayscale.neutral_500,
      **kwargs,
    )

    # Fires when the inner content size changes (children resize).
    self.bind("<Configure>",
      self._update_scrollbar_visibility, add=True
    )

    # Fires when the visible viewport resizes (parent resize).
    self._parent_canvas.bind("<Configure>",
      self._update_scrollbar_visibility, add=True
    )



  def _update_scrollbar_visibility(self, _event=None) -> None:
    content_h = self.winfo_reqheight()
    canvas_h = self._parent_canvas.winfo_height()

    # Calculate border spacing so we can still see the border when scrollbar 
    # is shown or hidden, scrollbar can sometimes cover the border (doesn't look good)
    border_spacing = self._apply_widget_scaling(
      self._parent_frame.cget("corner_radius") + self._parent_frame.cget("border_width")
    )

    if content_h > canvas_h:
      # Not enough room for content, show scroll bar
      self._parent_canvas.grid_configure(padx=(border_spacing, 0))
      self._scrollbar.grid()
    else:
      # Is enough room for content, hide scroll bar
      self._scrollbar.grid_remove()
      self._parent_canvas.grid_configure(padx=(border_spacing, border_spacing))

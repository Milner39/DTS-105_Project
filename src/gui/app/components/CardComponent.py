from .. import type_defs as GuiTypes
from ..theme import Colors
from .FragmentComponent import FragmentComponent
from .ScrollableComponent import ScrollableComponent



class CardComponent(FragmentComponent):
  """
  | A bordered, scrollable card.
  |
  | Width is controlled by the parent (e.g. via a fixed-width grid column).
  | Height grows with content, capped at the parent's available space — the
    body scrolls when content exceeds that cap.
  |
  | Add content by using `card.content` as the master.
  """

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self.PADDING: int = 24


    self.content = ScrollableComponent(
      self,
      corner_radius=6,
      border_width=1,
      border_color=Colors.Surface.border,
    )
    self.content.pack(fill="x", padx=self.PADDING, pady=self.PADDING)


    # Run on resize function when card content or parent resizes
    master.bind("<Configure>", self._on_resize, add=True)
    self.after_idle(self._on_resize)



  def _on_resize(self, _event=None) -> None:
    """
    | Set the height of the card to be the smallest of:
      - The available vertical space
      - The height of the card's content
    """

    self.content.update_idletasks()
    content_h = self.content.winfo_reqheight()
    available_h = max(0, self.master.winfo_height() - (2 * self.PADDING))
    self.content.configure(height=min(content_h, available_h))

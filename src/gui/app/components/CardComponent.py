from .. import type_defs as GuiTypes
from ..theme import Colors, Sizes
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

    super().__init__(master,
      border_color=Colors.Grayscale.neutral_700,
      border_width=Sizes.Border.md,
      corner_radius=Sizes.Radius.lg
    )

    # Force height to be controlled by `height` property
    self.pack_propagate(False)


    self.scrollable = ScrollableComponent(self)
    self.content = self.scrollable.content


    # Run on resize function when card content or parent resizes
    master.bind("<Configure>", self._on_resize, add=True)
    self.after_idle(self._on_resize)



  def _on_resize(self, _event=None) -> None:
    """
    | Set the height of the card to be the smallest of:
      - The available vertical space
      - The height of the card's content
    """

    self.scrollable.update_idletasks()
    desired_height = self.scrollable.natural_bordered_height
    available_height = max(0, self.master.winfo_height())
    self.configure(height=min(desired_height, available_height))

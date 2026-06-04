from .. import type_defs as GuiTypes
from ..theme import Colors, Sizes
from .FragmentComponent import FragmentComponent



class ScoreCircleComponent(FragmentComponent):
  """
  | A circular badge indicating a 1-5 mood score via the colour.
  """

  def __init__(self,
    master: GuiTypes.CTkMasterT,
    score: int,
    size: int = Sizes.Dimension.xs,
  ):
    color = Colors.Mood.for_score(score)

    super().__init__(master,
      width=size,
      height=size,
      corner_radius=size // 2,
      fg_color=color
    )

    # Force a fixed square shape so it renders as a circle.
    self.grid_propagate(False)
    self.pack_propagate(False)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

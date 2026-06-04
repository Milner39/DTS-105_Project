import customtkinter as ctk

from ....components.FragmentComponent import FragmentComponent
from ....components.ScoreCircleComponent import ScoreCircleComponent
from ....theme import Colors, Fonts, Sizes
from .... import type_defs as GuiTypes



class LegendComponent(FragmentComponent):
  """Static 'Score: 1..5' colour key under the calendar"""

  SCORE_CIRCLE_SIZE = Sizes.Dimension.xs


  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    # Create legend label
    ctk.CTkLabel(self,
      text="Score:",
      font=Fonts.Body.sm(),
      text_color=Colors.Grayscale.neutral_500
    ).pack(side="left", padx=(0, Sizes.Spacing.sm))

    # Create legend items
    for score in range(1, 6):
      item = FragmentComponent(self)
      item.pack(side="left", padx=(0, Sizes.Spacing.md))

      score_circle = ScoreCircleComponent(item,
        score=score,
        size=self.SCORE_CIRCLE_SIZE
      )
      score_circle.pack(side="left")

      ctk.CTkLabel(item,
        text=str(score), font=Fonts.Body.sm(),
        text_color=Colors.Grayscale.neutral_500,
      ).pack(side="left", padx=(Sizes.Spacing.xs, 0))

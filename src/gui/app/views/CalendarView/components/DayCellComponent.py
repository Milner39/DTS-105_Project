from datetime import date
from typing import Callable
import customtkinter as ctk

from ....components.FragmentComponent import FragmentComponent
from ....components.ScoreCircleComponent import ScoreCircleComponent
from ....theme import Colors, Fonts, Sizes
from .... import type_defs as GuiTypes
from ....helpers import bind_tree



class DayCellComponent(FragmentComponent):
  """
  | A day cell in the calendar grid:
    - day number
    - mood score
  """

  SCORE_CIRCLE_SIZE = Sizes.Dimension.xs


  def __init__(self,
    master: GuiTypes.CTkMasterT,
    *,
    day: date,
    score: int | None,
    is_today: bool,
    is_selected: bool,
    is_future: bool,
    on_select: Callable[[date], None],
  ):
    is_highlighted = is_today or is_selected

    # Init self with styling
    super().__init__(master,
      corner_radius=Sizes.Radius.sm,
      border_width=Sizes.Border.md if is_highlighted else Sizes.Border.sm,
      border_color=Colors.Brand.secondary if is_highlighted else Colors.Surface.border,
      fg_color=Colors.Brand.secondary__transparent if is_selected else "transparent",
    )
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)


    # Colour the day number based on the day's state
    num_color = (
      Colors.Brand.secondary if is_today else
      Colors.Grayscale.neutral_700 if is_future else
      Colors.Grayscale.neutral_300
    )

    # Create the day number label
    ctk.CTkLabel(self,
      text=str(day.day),
      font=Fonts.Heading.xs() if is_today else Fonts.Body.md(),
      text_color=num_color,
    ).grid(row=0, column=0, pady=(Sizes.Spacing.xs, 0))

    # Show the mood score if the day has a log
    if score is not None:
      ScoreCircleComponent(self,
        score,
        size=self.SCORE_CIRCLE_SIZE
      ).grid(row=1, column=0, pady=(0, Sizes.Spacing.xs))
    elif not is_future:
      pass


    # Bind click event to select day
    bind_tree(self, "<Button-1>", lambda _e, d=day: on_select(d))

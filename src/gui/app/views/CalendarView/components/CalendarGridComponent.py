import calendar
from datetime import date
from typing import Callable
import customtkinter as ctk

from ....components.FragmentComponent import FragmentComponent
from ....theme import Colors, Fonts, Sizes
from .... import type_defs as GuiTypes
from ......database.models.MoodLogModel import MoodLogReadT
from .DayCellComponent import DayCellComponent



class CalendarGridComponent(FragmentComponent):
  """
  | A calendar month grid:
    - weekday headers
    - one cell per day
  """

  # Sets the weekday headers
  WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")


  def __init__(self,
    master: GuiTypes.CTkMasterT,
    *,
    on_select_day: Callable[[date], None],
  ):
    super().__init__(master)

    # Callback for when a day get's selected
    self._on_select_day = on_select_day


    self._grid_frame: GuiTypes.CTkFrameT | None = None

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)



  def render(self,
    view_month: date,
    logs_by_day: dict[date, MoodLogReadT],
    selected_day: date | None,
  ) -> None:
    """Render the component."""

    # Destroy the last draw
    if self._grid_frame is not None:
      self._grid_frame.destroy()


    # Create 7 uniform columns
    grid = FragmentComponent(self)
    grid.grid(row=0, column=0, sticky="nsew")
    for col in range(7): grid.grid_columnconfigure(col, weight=1, uniform="day")
    self._grid_frame = grid


    # Add the weekday headers
    for col, name in enumerate(self.WEEKDAYS):
      ctk.CTkLabel(grid,
        text=name, font=Fonts.Body.sm(),
        text_color=Colors.Grayscale.neutral_500,
      ).grid(row=0, column=col, pady=(0, Sizes.Spacing.xs))



    # Get a 2D list representing a month's calendar, each row represents a week.
    weeks = calendar.Calendar(firstweekday=0).monthdayscalendar(
      view_month.year, view_month.month
    )

    # Create a row in the grid for each week in the month.
    for r in range(1, len(weeks) + 1):
      grid.grid_rowconfigure(r, weight=1, uniform="week")

    # Populate the grid with the days of the month.
    today = date.today()
    for row, week in enumerate(weeks):
      for col, day in enumerate(week):

        # Skip padding days from previous / next month
        if day == 0: continue

        # Get the date object for the day and fetch the log
        day_date = date(view_month.year, view_month.month, day)
        log = logs_by_day.get(day_date)

        # Create the day cell
        cell = DayCellComponent(grid,
          day=day_date,
          score=log["score"] if log is not None else None,
          is_today=day_date == today,
          is_selected=day_date == selected_day,
          is_future=day_date > today,
          on_select=self._on_select_day,
        )
        cell.grid(row=row + 1, column=col, sticky="nsew", padx=2, pady=2)

from datetime import date
import customtkinter as ctk

from ....components.FragmentComponent import FragmentComponent
from ....components.LineGraphComponent import LineGraphComponent
from ....theme import Colors, Fonts, Sizes
from .... import type_defs as GuiTypes
from ......database.models.MoodLogModel import MoodLogReadT



class MonthStatsComponent(FragmentComponent):
  """
  | Monthly summary:
    - average score
    - days logged
    - trend graph
  """

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)



  def render(self,
    view_month: date,
    logs_by_day: dict[date, MoodLogReadT]
  ) -> None:
    """Render the component."""

    # Destroy the last draw
    for child in self.winfo_children():
      child.destroy()


    # How the month heading
    ctk.CTkLabel(self,
      text=f"{view_month.strftime('%B')} so far",
      font=Fonts.Heading.xs(), anchor="w",
    ).pack(fill="x")


    # Calculate the average score and number of logged days
    scores = [log["score"] for log in logs_by_day.values()]
    days = len(scores)
    avg_text = f"{(sum(scores) / days):.1f}" if days else "-"

    # Create the container for the monthly statistics
    stats = FragmentComponent(self)
    stats.pack(fill="x", pady=(Sizes.Spacing.sm, 0))
    stats.grid_columnconfigure(0, weight=1)
    stats.grid_columnconfigure(1, weight=1)
    self._stat_box(stats, 0, avg_text, "Avg score")
    self._stat_box(stats, 1, str(days), "Days logged")


    # Create the chart title
    ctk.CTkLabel(self,
      text="This month's trend",
      font=Fonts.Body.sm(),
      text_color=Colors.Grayscale.neutral_500, 
      anchor="w"
    ).pack(fill="x", pady=(Sizes.Spacing.sm, Sizes.Spacing.xs))

    # Plot the month's scores in date order
    ordered = [logs_by_day[d]["score"] for d in sorted(logs_by_day)]
    LineGraphComponent(self, data=ordered, height=Sizes.Dimension.xl).pack(fill="x")



  def _stat_box(self,
    master: GuiTypes.CTkMasterT,
    col: int,
    value: str,
    label: str
  ) -> None:
    """
    | Create a bordered stat box: 
      - bold value
      - subtle caption
    """

    # Create the box
    box = FragmentComponent(master,
      border_width=Sizes.Border.sm, 
      border_color=Colors.Surface.border,
      corner_radius=Sizes.Radius.sm,
    )
    pad = (0, Sizes.Spacing.xs) if col == 0 else (Sizes.Spacing.xs, 0)
    box.grid(row=0, column=col, sticky="ew", padx=pad)

    # Show the value and caption labels
    ctk.CTkLabel(box,
      text=value,
      font=Fonts.Heading.sm(),
      text_color=Colors.Brand.secondary
    ).pack(pady=(Sizes.Spacing.sm, 0))
    ctk.CTkLabel(box,
      text=label,
      font=Fonts.Body.sm(),
      text_color=Colors.Grayscale.neutral_500,
    ).pack(pady=(0, Sizes.Spacing.sm))

from datetime import date
import customtkinter as ctk

from ...components.FragmentComponent import FragmentComponent
from ...components.ScrollableComponent import ScrollableComponent
from ...layouts.WithViewTitleLayout import WithViewTitleLayout
from ...stores.NavigationStore import navigation_store
from ...stores.LogEditorStore import log_editor_store
from ...theme import Colors, Sizes
from ... import type_defs as GuiTypes
from .....database import Queries
from .....database.models.MoodLogModel import MoodLogReadT
from .components.MonthNavComponent import MonthNavComponent
from .components.CalendarGridComponent import CalendarGridComponent
from .components.LegendComponent import LegendComponent
from .components.SelectedLogComponent import SelectedLogComponent
from .components.MonthStatsComponent import MonthStatsComponent



class CalendarView(FragmentComponent):
  """The `log calendar` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.SIDE_PANEL_WIDTH = Sizes.Dimension.xxl * 2


    today = date.today()
    self._view_month: date = today.replace(day=1)
    """Currently selected month and year"""

    self._selected_day: date | None = today
    """Currently selected day"""

    self._logs_by_day: dict[date, MoodLogReadT] = {}
    "Current month's logs by date"


    view_title_layout = WithViewTitleLayout(self, "Log Calendar")
    content = view_title_layout.set_content(FragmentComponent)
    content.grid_rowconfigure(0, weight=0)
    content.grid_rowconfigure(1, weight=1)
    content.grid_columnconfigure(0, weight=1)

    self._build_nav(content)
    self._build_body(content)

    self._refresh()



  # === Layout =================================================================

  def _build_nav(self, parent: GuiTypes.CTkMasterT) -> None:
    """
    | Month switcher row:
      - prev
      - month label
      - next
      - 'Log Today' button
    """

    self._calendar_nav_comp = MonthNavComponent(parent,
      on_prev=lambda: self._shift_month(-1),
      on_next=lambda: self._shift_month(1),
      on_log_today=self._open_log_today,
    )
    self._calendar_nav_comp.grid(row=0, column=0, sticky="ew",
      padx=Sizes.Spacing.md, pady=(Sizes.Spacing.sm, Sizes.Spacing.none)
    )


  def _build_body(self, parent: GuiTypes.CTkMasterT) -> None:
    """
    | Two columns:
      - calendar (responsive)
      - divider
      - side panel
    """

    body = FragmentComponent(parent)
    body.grid(row=1, column=0, sticky="nsew")
    body.grid_rowconfigure(0, weight=1)
    body.grid_columnconfigure(0, weight=1)
    body.grid_columnconfigure(1, weight=0, minsize=Sizes.Border.md)
    body.grid_columnconfigure(2, weight=0, minsize=self.SIDE_PANEL_WIDTH)

    # Calendar panel (grid + legend)
    cal_panel = FragmentComponent(body)
    cal_panel.grid(row=0, column=0, sticky="nsew",
      padx=Sizes.Spacing.md, pady=Sizes.Spacing.sm
    )
    cal_panel.grid_columnconfigure(0, weight=1)
    cal_panel.grid_rowconfigure(0, weight=1)
    cal_panel.grid_rowconfigure(1, weight=0)

    self._calendar_grid_comp = CalendarGridComponent(cal_panel,
      on_select_day=self._select_day,
    )
    self._calendar_grid_comp.grid(row=0, column=0, sticky="nsew")

    LegendComponent(cal_panel).grid(row=1, column=0, sticky="ew",
      pady=(Sizes.Spacing.sm, 0)
    )

    # Divider
    divider = FragmentComponent(body,
      width=Sizes.Border.md, fg_color=Colors.Surface.border
    )
    divider.grid(row=0, column=1, sticky="ns")
    divider.grid_propagate(False)

    # Side panel
    side = FragmentComponent(body)
    side.grid(row=0, column=2, sticky="nsew")
    side_scroll = ScrollableComponent(side)
    side_content = side_scroll.content

    self._selected_log_comp = SelectedLogComponent(side_content,
      on_edit=self._edit_selected,
      on_delete=self._delete_selected,
    )
    self._selected_log_comp.pack(fill="x")

    ctk.CTkFrame(side_content,
      height=Sizes.Border.sm, fg_color=Colors.Surface.border,
    ).pack(fill="x", pady=Sizes.Spacing.sm)

    self._stats_comp = MonthStatsComponent(side_content)
    self._stats_comp.pack(fill="x")



  # === Data & state ===========================================================

  def _load_data(self) -> None:
    """Get the selected month's logs."""
    self._logs_by_day = {}
    for log in Queries.MoodLog.list_logs():
      d = log["logged_at"].date()
      if d.year == self._view_month.year and d.month == self._view_month.month:
        self._logs_by_day[d] = log


  def _shift_month(self, delta: int) -> None:
    """
    | Change the selected month by +/- a number of months.
    | Handles year changes by using `months DIV 12` and `months MOD 12`
    """
    months = self._view_month.month - 1 + delta
    year = self._view_month.year + months // 12
    month = months % 12 + 1
    self._view_month = date(year, month, 1)

    # Clear selected day when month changes
    self._selected_day = None

    self._refresh()


  def _select_day(self, day: date) -> None:
    """Change the selected day."""
    self._selected_day = day

    # Re-render required widgets
    self._calendar_grid_comp.render(self._view_month, self._logs_by_day, self._selected_day)
    self._selected_log_comp.render(
      self._selected_day, self._logs_by_day.get(self._selected_day)
    )


  def _open_log_today(self) -> None:
    """
    | Update the log editor store to target today and navigate to 
      the `new-log` view.
    """
    log_editor_store.set_target(date.today())
    navigation_store.navigate("new-log")


  def _edit_selected(self) -> None:
    """
    | Update the log editor store to target the selected log and navigate to 
      the `new-log` view.
    """
    if self._selected_day is None:
      return
    log_editor_store.set_target(self._selected_day)
    navigation_store.navigate("new-log")


  def _delete_selected(self) -> None:
    """Delete the selected log."""

    if self._selected_day is None:
      return

    log = self._logs_by_day.get(self._selected_day)
    if log is None:
      return

    Queries.MoodLog.delete_log({"id": log["id"]})
    self._refresh()



  # === Rendering ==============================================================

  def _refresh(self) -> None:
    """Reload data and refresh every widget."""
    self._load_data()
    self._calendar_nav_comp.set_month(self._view_month)
    self._calendar_grid_comp.render(self._view_month, self._logs_by_day, self._selected_day)
    self._selected_log_comp.render(
      self._selected_day,
      self._logs_by_day.get(self._selected_day) if self._selected_day is not None else None
    )
    self._stats_comp.render(self._view_month, self._logs_by_day)

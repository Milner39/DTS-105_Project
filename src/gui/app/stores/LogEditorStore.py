from . import Store
from dataclasses import dataclass
from datetime import date



@dataclass
class LogEditorState:
  # Which day the log editor (NewLogView) should load and save.
  target_date: date



class LogEditorStore(Store[LogEditorState]):
  """
  | Holds the day the log editor should open on.
  |
  | Views are constructed by the router with no arguments, this was a planned
    feature but scrapped due to time constraints. So the fast solution is using
    a store.
  |
  | The calendar's "edit" action communicates the target day to `NewLogView`
    through this store. Buttons like "log today" reset it using `set_target`.
  """

  def __init__(self):
    super().__init__(LogEditorState(target_date=date.today()))

  def set_target(self, target_date: date) -> None:
    """Set the day the editor should open on."""
    self.patch_state(lambda _s: LogEditorState(target_date=target_date))



log_editor_store = LogEditorStore()

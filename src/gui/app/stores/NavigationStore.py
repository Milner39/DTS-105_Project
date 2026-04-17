from . import Store
from ..router import router
from dataclasses import dataclass, field



@dataclass
class NavigationState:
  current_route: list[str] = field(default_factory=list)



class NavigationStore(Store[NavigationState]):
  def __init__(self):
    super().__init__(NavigationState())

  def navigate(self, path: str) -> None:
    """
    | Navigate to the given route path.
    | Path segments are split on `/`, e.g. `"settings/profile"` → `["settings", "profile"]`
    """
    segments = [s for s in path.split("/") if s]
    self.patch_state(lambda s: NavigationState(current_route=segments))


  def get_views(self):
    """Get the corresponding views for the current route."""
    return router.resolve_route(self.get_state().current_route)



navigation_store = NavigationStore()

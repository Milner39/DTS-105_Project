from . import Store
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
    # Lazy import: the router module imports every view class, and any view
    # in the tree that wants to call `navigation_store.navigate(...)` would
    # otherwise create a circular import at module-load time.
    from ..router import router
    return router.resolve_route(self.get_state().current_route)



navigation_store = NavigationStore()

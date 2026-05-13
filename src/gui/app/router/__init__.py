from .. import type_defs as GuiTypes
from ..views.DashboardView import DashboardView
from ..views.NewLogView import NewLogView



"""
Routes have a `is_layout` flag.
This flag dictates how the views for the route should be rendered.

Let's say we have this full route:
root (is_layout) => with_sidebar (is_layout) => dashboard

`root` will be rendered
`with_sidebar` will be rendered inside of that
`dashboard` will be rendered inside of that


Now let's add another view so we have this full route:
root (is_layout) => with_sidebar (is_layout) => dashboard => settings

`root` will be rendered
`with_sidebar` will be rendered inside of that
`settings` will be rendered inside of that

See how we don't render `dashboard`?


The flag is intended to tell the router if a "sub view" should be rendered
inside a parent view.
"""



class RouteNotFoundError(Exception):
  """Raised when a route path cannot be resolved to a view"""
  pass



class Route:
  """
  | Route class
  | Used for building the Gui navigation.
  |
  | Resembles a tree data structure with each instance of this class acting as a node.
  """

  def __init__(
    self,
    path: str,
    view: type[GuiTypes.CTkFrameT] | None,
    *,
    children: list["Route"] | None = None,
    is_layout: bool = False
  ):
    self.path: str = path
    self.view: type[GuiTypes.CTkFrameT] | None = view
    self._children: list["Route"] = children if children is not None else []
    self.is_layout: bool = is_layout



  @property
  def child_paths(self) -> dict[str, "Route"]:
    return { route.path: route for route in self._children }



  def resolve_route(
    self,
    path_segments: list[str],
    views: list[type[GuiTypes.CTkFrameT]] | None = None,
    from_root: bool = True
  ) -> list[type[GuiTypes.CTkFrameT]]:
    """
    | Recursively walk the route tree, building up the list of views to render.
    |
    | `path_segments`: remaining path segments yet to be matched
    | `views`: accumulated list of views to render, built up across recursive calls
    | `from_root`: whether this call is the root of the recursion — used to wrap
    |   the error with the full path, which child calls don't have access to
    """

    if views is None:
      views = []


    # No more segments to match so this is the target view
    if len(path_segments) == 0:
      if self.view is None:
        raise RouteNotFoundError("Route has no view")

      views.append(self.view)
      return views


    # Layout views are always rendered
    if self.is_layout and self.view is not None:
      views.append(self.view)


    # Advance to the next segment and recurse into the matching child
    path = path_segments[0]
    if path not in self.child_paths:
      raise RouteNotFoundError(f"No child route '{path}'")


    try:
      self.child_paths[path].resolve_route(path_segments[1:], views, False)
    except RouteNotFoundError as e:
      # Only the root call re-raises with the full path
      if not from_root:
        raise
      raise RouteNotFoundError(
        f"Route not found: /{'/'.join(path_segments)}"
      ) from e

    return views



router = Route(path="", view=None,
  children=[
    Route(path="dashboard", view=DashboardView),
    Route(path="new-log", view=NewLogView)
  ]
)

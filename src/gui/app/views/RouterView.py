from typing import Unpack
from .. import type_defs as GuiTypes
from ..components.FragmentComponent import FragmentComponent



class RouterView(FragmentComponent):
  """
  | View class to extend when creating real views.
  |
  | Extend this class in any view that needs to render child routes inside itself.
  | When a route resolves to multiple views, each RouterView in the chain renders
  | the next view in the list, enabling nested routing.
  """

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    **kwargs: Unpack[GuiTypes.CTkFrameKwargsT]
  ):
    super().__init__(master, **kwargs)

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    # Container frame that the active route content is rendered inside
    self._router_area = FragmentComponent(self)
    self._router_area.grid(row=0, column=0, sticky="nsew")
    self._router_area.grid_rowconfigure(0, weight=1)
    self._router_area.grid_columnconfigure(0, weight=1)
    self._router_content: GuiTypes.CTkFrameT | None = None



  def render_route(self, views: list[type[GuiTypes.CTkFrameT]]) -> None:
    """
    | Render the first view in the list, then pass remaining views down if the
    | rendered view is itself a RouterView (enabling nested routing).
    """

    view_count = len(views)
    if view_count < 1: return

    # Destroy the previous route content before rendering the new one
    if self._router_content is not None:
      self._router_content.destroy()

    self._router_content = views[0](self._router_area)
    self._router_content.grid(row=0, column=0, sticky="nsew")

    # If there are remaining views and the rendered view can host children, pass them down
    if view_count > 1 and isinstance(self._router_content, RouterView):
      self._router_content.render_route(views[1:])

from typing import Unpack
from .. import type_defs as GuiTypes
from ..components.FragmentComponent import FragmentComponent



class RouterView(FragmentComponent):
  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    **kwargs: Unpack[GuiTypes.CTkFrameKwargsT]
  ):
    super().__init__(master, **kwargs)

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self._router_area = FragmentComponent(self)
    self._router_area.grid(row=0, column=1, sticky="nsew")
    self._router_area.grid_rowconfigure(0, weight=1)
    self._router_area.grid_columnconfigure(0, weight=1)
    self._router_content: GuiTypes.CTkFrameT | None = None



  def render_route(self, views: list[type[GuiTypes.CTkFrameT]]) -> None:
    """Lets a parent router view pass the correct router content down the views"""

    view_count = len(views)
    if view_count < 1: return

    self._router_content = views[0](self._router_area)
    if view_count > 1 and isinstance(self._router_content, RouterView):
      self._router_content.render_route(views[1:])

from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes
from ..components.SidebarNavComponent import SidebarNavComponent
from ..stores.NavigationStore import navigation_store, NavigationState
from ..router import router, RouteNotFoundError



class WithSidebarLayout(FragmentComponent):
  """Sidebar and content layout"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self._sidebar_area:   GuiTypes.CTkFrameT
    self._content_area:   GuiTypes.CTkFrameT
    self.active_sidebar:  SidebarNavComponent
    self.active_content:  GuiTypes.CTkFrameT | None = None


    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)


    sidebar_area = FragmentComponent(self)
    sidebar_area.grid(row=0, column=0, sticky="ns")
    sidebar_area.grid_rowconfigure(0, weight=1)
    sidebar_area.grid_columnconfigure(0, weight=1)
    self._sidebar_area = sidebar_area

    active_sidebar = SidebarNavComponent(sidebar_area)
    active_sidebar.grid(row=0, column=0, sticky="ns")
    self.active_sidebar = active_sidebar

    content_area = FragmentComponent(self)
    content_area.grid(row=0, column=1, sticky="nsew")
    content_area.grid_rowconfigure(0, weight=1)
    content_area.grid_columnconfigure(0, weight=1)
    self._content_area = content_area

    self._unsubscribe = navigation_store.subscribe(self._on_navigate)



  def _on_navigate(self, state: NavigationState, _prev: NavigationState) -> None:
    if not state.current_route:
      return

    try:
      views = router.resolve_route(state.current_route)
    except RouteNotFoundError:
      return

    if views:
      self.set_content(views[-1])



  def destroy(self) -> None:
    self._unsubscribe()
    super().destroy()



  def set_content(self, content: type[GuiTypes.CTkFrameTG], *args, **kwargs) -> GuiTypes.CTkFrameTG:
    """Replace current content"""

    if self.active_content is not None:
      self.active_content.destroy()

    active_content = content(self._content_area, *args, **kwargs)
    active_content.grid(row=0, column=0, sticky="nsew")
    self.active_content = active_content
    return self.active_content

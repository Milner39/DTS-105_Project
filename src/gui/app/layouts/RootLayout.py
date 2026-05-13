from . import Layout
from .. import type_defs as GuiTypes
from ..stores.NavigationStore import navigation_store
from .WithSidebarLayout import WithSidebarLayout
from ..views.RouterView import RouterView
from ..components.ButtonsSidebarComponent import Button



class RootLayout(Layout):
  """Top-level layout"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)


    self.grid(row=0, column=0, sticky="nsew")
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)


    sidebar_layout = WithSidebarLayout(self)

    self._sidebar_buttons = [
      ("dashboard", sidebar_layout.sidebar.add_button(
        icon="house-line",
        command=lambda: navigation_store.navigate("dashboard"),
      )),
      ("new-log", sidebar_layout.sidebar.add_button(
        icon="notepad",
        command=lambda: navigation_store.navigate("new-log"),
      ))
    ]

    self._sidebar_layout = sidebar_layout


    router_view = sidebar_layout.set_content(RouterView)
    self._router_view = router_view

    navigation_store.subscribe(self._on_navigation_update)



  def set_content(self, new_content: type[GuiTypes.CTkFrameTG], *args, **kwargs) -> GuiTypes.CTkFrameTG:
    content = super().set_content(new_content, *args, **kwargs)

    content.grid(row=0, column=0, sticky="nsew")

    return content


  def _on_navigation_update(self, *args):
    self._router_view.render_route(navigation_store.get_views())

    current_route = navigation_store.get_state().current_route

    # Configure button colors
    for route, btn in self._sidebar_buttons:
      btn.set_active(bool(current_route) and current_route[0] == route)

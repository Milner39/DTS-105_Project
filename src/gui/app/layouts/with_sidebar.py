import customtkinter as _ctk
from .. import type_defs as GuiTypes
from ..components.SidebarNav import SidebarNav__Component as SidebarNav
from ...assets import AssetUtils



class WithSidebar__Layout(_ctk.CTkFrame):
  """Sidebar and content layout"""

  _sidebar_area:    _ctk.CTkFrame | None = None
  _active_sidebar:  _ctk.CTkFrame | None = None
  _content_area:    _ctk.CTkFrame | None = None
  _active_content:  _ctk.CTkFrame | None = None



  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master, fg_color="transparent")

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)


    sidebar_area = _ctk.CTkFrame(self, fg_color="transparent")
    sidebar_area.grid(row=0, column=0, sticky="ns")
    sidebar_area.grid_rowconfigure(0, weight=1)
    sidebar_area.grid_columnconfigure(0, weight=1)
    self._sidebar_area = sidebar_area

    active_sidebar = SidebarNav(sidebar_area)
    active_sidebar.grid(row=0, column=0, sticky="ns")
    active_sidebar.add_button(image=AssetUtils.ctk_icon("house-line"))
    active_sidebar.add_button(image=AssetUtils.ctk_icon("notepad"))
    self._active_sidebar = active_sidebar


    content_area = _ctk.CTkFrame(self, fg_color="transparent")
    content_area.grid(row=0, column=1, sticky="nsew")
    content_area.grid_rowconfigure(0, weight=1)
    content_area.grid_columnconfigure(0, weight=1)
    self._content_area = content_area



  def set_content(self, content: type[GuiTypes.CTkFrameT], *args, **kwargs) -> GuiTypes.CTkFrameT:
    """Replace current content"""

    if self._active_content is not None:
      self._active_content.destroy()

    active_content = content(self._content_area, *args, **kwargs)
    active_content.grid(row=0, column=0, sticky="nsew")
    self._active_content = active_content
    return self._active_content
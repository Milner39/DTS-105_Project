from . import Layout
from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes
from ..components.ButtonsSidebarComponent import ButtonsSidebarComponent



class WithSidebarLayout(Layout):
  """Sidebar and content layout"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self._sidebar_area:   GuiTypes.CTkFrameT
    self._content_area:   GuiTypes.CTkFrameT
    self.sidebar:  ButtonsSidebarComponent


    self.grid(row=0, column=0, sticky="nsew")
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)


    sidebar_area = FragmentComponent(self)
    sidebar_area.grid(row=0, column=0, sticky="ns")
    sidebar_area.grid_rowconfigure(0, weight=1)
    sidebar_area.grid_columnconfigure(0, weight=1)
    self._sidebar_area = sidebar_area

    sidebar = ButtonsSidebarComponent(sidebar_area)
    sidebar.grid(row=0, column=0, sticky="ns")
    self.sidebar = sidebar


    content_area = FragmentComponent(self)
    content_area.grid(row=0, column=1, sticky="nsew")
    content_area.grid_rowconfigure(0, weight=1)
    content_area.grid_columnconfigure(0, weight=1)
    self._content_area = content_area



  def set_content(self, new_content: type[GuiTypes.CTkFrameTG], *args, **kwargs) -> GuiTypes.CTkFrameTG:
    content = super().set_content(new_content, self._content_area, *args, **kwargs)

    content.grid(row=0, column=0, sticky="nsew")

    return content

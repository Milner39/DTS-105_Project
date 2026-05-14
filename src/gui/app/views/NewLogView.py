import customtkinter as ctk
from ..components.FragmentComponent import FragmentComponent
from ..layouts.WithViewTitleLayout import WithViewTitleLayout
from .. import type_defs as GuiTypes
from ...assets import AssetUtils



class NewLogView(FragmentComponent):
  """The `new log` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)


    view_title_layout = WithViewTitleLayout(self, "New Log")
    content = view_title_layout.set_content(FragmentComponent)

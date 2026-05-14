import customtkinter as ctk
from ..components.FragmentComponent import FragmentComponent
from ..layouts.WithViewTitleLayout import WithViewTitleLayout
from .. import type_defs as GuiTypes
from ...assets import AssetUtils



class CalendarView(FragmentComponent):
  """The `log calendar` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)


    view_title_layout = WithViewTitleLayout(self, "Log Calender")
    content = view_title_layout.set_content(FragmentComponent)

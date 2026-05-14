import customtkinter as ctk
from ..components.FragmentComponent import FragmentComponent
from ..layouts.WithViewTitleLayout import WithViewTitleLayout
from .. import type_defs as GuiTypes
from ...assets import AssetUtils



class DashboardView(FragmentComponent):
  """The `home` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)


    view_title_layout = WithViewTitleLayout(self, "Home")
    content = view_title_layout.set_content(FragmentComponent)

    logo = AssetUtils.ctk_icon("moodminder-logo", 128)
    logo_label = ctk.CTkLabel(content, text="", image=logo)
    logo_label.pack()

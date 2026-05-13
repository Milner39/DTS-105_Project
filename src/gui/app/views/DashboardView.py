import customtkinter as ctk
from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes
from ...assets import AssetUtils as AssetUtils



class DashboardView(FragmentComponent):
  """The `dashboard` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    ctk.CTkLabel(self, text="Dashboard").pack(padx=12, pady=12)

    logo = AssetUtils.ctk_icon("moodminder-logo", 128)
    logo_label = ctk.CTkLabel(self, text="", image=logo)
    logo_label.pack()

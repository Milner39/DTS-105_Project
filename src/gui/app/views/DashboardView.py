import customtkinter as ctk
from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes



class Dashboard__View(FragmentComponent):
  """The `dashboard` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    ctk.CTkLabel(self, text="Dashboard").pack(padx=12, pady=12)

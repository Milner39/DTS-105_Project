import customtkinter as _ctk
from ...components.widgets.Fragment import Fragment
from ... import type_defs as GuiTypes



class Dashboard__View(Fragment):
  """The `dashboard` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    _ctk.CTkLabel(self, text="Dashboard").pack(padx=12, pady=12)

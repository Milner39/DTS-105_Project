import customtkinter as _ctk
from ...components.widgets.Fragment import Fragment
from ... import type_defs as GuiTypes



class NewLog__View(Fragment):
  """The `new log` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    _ctk.CTkLabel(self, text="New Log").pack(padx=12, pady=12)

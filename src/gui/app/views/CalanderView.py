import customtkinter as ctk
from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes



class CalendarView(FragmentComponent):
  """The `calendar` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    ctk.CTkLabel(self, text="Log Calendar").pack(padx=12, pady=12)

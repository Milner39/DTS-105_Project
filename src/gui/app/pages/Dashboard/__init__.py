import customtkinter as ctk
from ... import type_defs as GuiTypes



class Dashboard__Page(ctk.CTkFrame):
  """The dashboard page"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master, fg_color="transparent")
    ctk.CTkLabel(self, text="Dashboard").pack(padx=12, pady=12)
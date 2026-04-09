import customtkinter as _ctk
from ... import type_defs as GuiTypes
from .sidebar_button import SidebarNav_Button as Button



class SidebarNav__Component(_ctk.CTkFrame):
  """Sidebar container (nav rail + border)."""

  NAV_WIDTH = 48
  BORDER_WIDTH = 2


  _nav:     _ctk.CTkFrame | None = None
  _border:  _ctk.CTkFrame | None = None

  _next_row = 0



  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master, fg_color="transparent")

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=0, minsize=self.NAV_WIDTH)
    self.grid_columnconfigure(1, weight=0, minsize=self.BORDER_WIDTH)

    nav = _ctk.CTkFrame(self, width=self.NAV_WIDTH, corner_radius=0, fg_color="transparent")
    nav.grid(row=0, column=0, sticky="ns")
    nav.grid_columnconfigure(0, weight=1)
    nav.grid_propagate(False)
    self._nav = nav

    border = _ctk.CTkFrame(self, width=self.BORDER_WIDTH, corner_radius=0, fg_color=("gray80", "gray30"))
    border.grid(row=0, column=1, sticky="nsew")
    border.grid_propagate(False)
    self._border = border


  def add_button(self, *, command=None, image=None) -> Button:
    btn = Button(self._nav, height=self.NAV_WIDTH, command=command, image=image)
    btn.grid(row=self._next_row, column=0, sticky="ew")
    self._next_row += 1
    return btn
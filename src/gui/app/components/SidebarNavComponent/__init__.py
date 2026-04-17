from ..FragmentComponent import FragmentComponent
from ... import type_defs as GuiTypes
from .button import Button



class SidebarNavComponent(FragmentComponent):
  """Sidebar container (nav rail + border)."""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self.NAV_WIDTH: int = 48
    self.BORDER_WIDTH: int = 2

    self.nav:     GuiTypes.CTkFrameT
    self.border:  GuiTypes.CTkFrameT

    self._next_row: int = 0


    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=0, minsize=self.NAV_WIDTH)
    self.grid_columnconfigure(1, weight=0, minsize=self.BORDER_WIDTH)


    nav = FragmentComponent(self, width=self.NAV_WIDTH, corner_radius=0)
    nav.grid(row=0, column=0, sticky="ns")
    nav.grid_columnconfigure(0, weight=1)
    nav.grid_propagate(False)
    self.nav = nav

    border = FragmentComponent(self, width=self.BORDER_WIDTH, corner_radius=0, fg_color=("gray80", "gray30"))
    border.grid(row=0, column=1, sticky="nsew")
    border.grid_propagate(False)
    self.border = border



  def add_button(self, *, command=None, image=None) -> Button:
    btn = Button(self.nav, height=self.NAV_WIDTH, command=command, image=image)
    btn.grid(row=self._next_row, column=0, sticky="ew")
    self._next_row += 1
    return btn

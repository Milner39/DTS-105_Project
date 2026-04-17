from ..FragmentComponent import FragmentComponent
from ... import type_defs as GuiTypes
from .button import Button



class ButtonsSidebarComponent(FragmentComponent):
  """
  | A sidebar with buttons.
  |
  | Sidebar also creates a visual border between the sidebar and the rest of 
    the content.
  |
  | This component is only the sidebar itself, it needs to be used within a 
    layout for other content to be visible.
  """

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self.BAR_WIDTH: int = 48
    self.BORDER_WIDTH: int = 2

    self.bar:     GuiTypes.CTkFrameT
    self.border:  GuiTypes.CTkFrameT

    self._next_row: int = 0


    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=0, minsize=self.BAR_WIDTH)
    self.grid_columnconfigure(1, weight=0, minsize=self.BORDER_WIDTH)


    bar = FragmentComponent(self, width=self.BAR_WIDTH, corner_radius=0)
    bar.grid(row=0, column=0, sticky="ns")
    bar.grid_columnconfigure(0, weight=1)
    bar.grid_propagate(False)
    self.bar = bar

    border = FragmentComponent(self, width=self.BORDER_WIDTH, corner_radius=0, fg_color=("gray80", "gray30"))
    border.grid(row=0, column=1, sticky="nsew")
    border.grid_propagate(False)
    self.border = border



  def add_button(self, *, command=None, image=None) -> Button:
    """Add a button to the sidebar"""

    btn = Button(self.bar, height=self.BAR_WIDTH, command=command, image=image)
    btn.grid(row=self._next_row, column=0, sticky="ew")
    self._next_row += 1
    return btn

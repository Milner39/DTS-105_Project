import customtkinter as _ctk
from ... import type_defs as GuiTypes



class SidebarNav_Button(_ctk.CTkButton):
  """Default-styled button for sidebar navigation."""

  def __init__(self, master: GuiTypes.CTkMasterT, *, height: int, command=None, image=None):
    super().__init__(
      master=master,
      height=height,
      text="",
      command=command,
      image=image,
      corner_radius=0,
      fg_color="transparent",
      hover_color=("gray88", "gray22"),
      anchor="center",
    )

import customtkinter as ctk
from ... import type_defs as GuiTypes



class Button(ctk.CTkButton):
  """Styled button for sidebar"""

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

import customtkinter as _ctk
from .. import type_defs as GuiTypes



class Root__Layout(_ctk.CTkFrame):
  """Top-level layout container"""

  _active_layout: _ctk.CTkFrame | None = None


  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master, fg_color="transparent")

    self.grid(row=0, column=0, sticky="nsew")
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)


  def set_layout(self, layout: type[GuiTypes.CTkFrameT], *args, **kwargs) -> GuiTypes.CTkFrameT:
    """Replace current child layout (e.g. with sidebar layout)."""

    if self._active_layout is not None:
      self._active_layout.destroy()

    active_layout = layout(self, *args, **kwargs)
    active_layout.grid(row=0, column=0, sticky="nsew")
    self._active_layout = active_layout
    return self._active_layout
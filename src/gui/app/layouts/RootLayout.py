from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes



class RootLayout(FragmentComponent):
  """Top-level layout container"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self._active_layout: GuiTypes.CTkFrameT | None = None


    self.grid(row=0, column=0, sticky="nsew")
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)



  def set_layout(self, layout: type[GuiTypes.CTkFrameTG], *args, **kwargs) -> GuiTypes.CTkFrameTG:
    """Replace current child layout (e.g. with sidebar layout)."""

    if self._active_layout is not None:
      self._active_layout.destroy()

    active_layout = layout(self, *args, **kwargs)
    active_layout.grid(row=0, column=0, sticky="nsew")
    self._active_layout = active_layout
    return self._active_layout

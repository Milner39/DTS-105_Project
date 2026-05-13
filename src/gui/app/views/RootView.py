from ..layouts.RootLayout import RootLayout
from .. import type_defs as GuiTypes



class RootView(RootLayout):
  """The root view that is always rendered while the GUI is running"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

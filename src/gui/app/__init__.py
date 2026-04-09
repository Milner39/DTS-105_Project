import customtkinter as _ctk
from .config import Config as _Config
from .layouts.root import Root__Layout as _Root__layout
from .layouts.with_sidebar import WithSidebar__Layout as _WithSidebar__layout
from .pages.Dashboard import Dashboard__Page as _Dashboard__Page
from ..assets import AssetUtils as _AssetUtils



class App(_ctk.CTk):
  def __init__(self):
    super().__init__()



class Gui():
  """Class containing methods for using the GUI"""

  # create CTk app
  app = App()
  ctk = _ctk


  @staticmethod
  def prepare():
    """
    | Run required scripts.

    | For fast start times, these scripts should be implemented in a way that they don't run from scratch every 
    execution,e.g: SVGs are only converted into PNGs if the PNG file does not already exists or is outdated.
    """

    _AssetUtils.prepare_assets()
    _Config.apply_config(__class__.app)


  @staticmethod
  def mainloop():
    """Start the GUI"""

    # Run pre-requisites (prepare assets, etc)
    __class__.prepare()

    # Render root layout
    app = __class__.app
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    root = _Root__layout(app)
    with_sidebar = root.set_layout(_WithSidebar__layout)
    with_sidebar.set_content(_Dashboard__Page)

    __class__.app.mainloop()

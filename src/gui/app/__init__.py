import customtkinter as _ctk
from .config import Config as _Config
from .layouts.root import Root__Layout as _Root__layout
from .layouts.with_sidebar import WithSidebar__Layout as _WithSidebar__layout
from ..assets import AssetUtils as _AssetUtils
from .stores.navigation import navigation_store as _navigation_store



class App(_ctk.CTk):
  def __init__(self):
    super().__init__()



class Gui():
  """Class containing methods for using the GUI"""

  @classmethod
  def prepare(cls) -> None:
    """
    | Run required scripts.

    | For fast start times, these scripts should be implemented in a way that they don't run from scratch every
    execution, e.g: SVGs are only converted into PNGs if the PNG file does not already exist or is outdated.
    """

    _AssetUtils.prepare_assets()


  @classmethod
  def mainloop(cls) -> None:
    """Start the GUI"""

    app = App()
    _Config.apply_config(app)

    # Run pre-requisites (prepare assets, etc)
    cls.prepare()

    # Render root layout
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    root = _Root__layout(app)
    with_sidebar = root.set_layout(_WithSidebar__layout)
    with_sidebar.active_sidebar.add_button(
      image=_AssetUtils.ctk_icon("house-line"),
      command=lambda: _navigation_store.navigate("dashboard")
    )
    with_sidebar.active_sidebar.add_button(
      image=_AssetUtils.ctk_icon("notepad"),
      command=lambda: _navigation_store.navigate("new-log")
    )

    _navigation_store.navigate("dashboard")

    app.mainloop()

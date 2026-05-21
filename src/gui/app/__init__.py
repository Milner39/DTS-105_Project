import customtkinter as ctk
from .config import Config
from ..assets import AssetUtils
from .stores.NavigationStore import navigation_store
from .views.RootView import RootView



class App(ctk.CTk):
  """The customtkinter app"""

  def __init__(self):
    """Initialise the app and apply the config"""
    super().__init__()
    Config.apply_config(self)



class Gui():
  """Class containing methods for using the GUI"""

  @classmethod
  def prepare(cls) -> None:
    """
    | Run required scripts.
    |
    | For fast start times, these scripts should be implemented in a way that 
      they don't run from scratch every execution, e.g: SVGs are only converted 
      into PNGs if the PNG file does not already exist or is outdated.
    """

    AssetUtils.prepare_assets()


  @classmethod
  def mainloop(cls) -> None:
    """Start the GUI"""

    # Create the app
    app = App()

    # Run pre-requisites (prepare assets, etc)
    cls.prepare()

    # Create a 1 col, 1 row grid for content
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    # Create and render the root layout
    root = RootView(app)

    # Navigate to landing page
    navigation_store.navigate("dashboard")

    # Start the app
    app.mainloop()

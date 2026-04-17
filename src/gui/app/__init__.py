import customtkinter as ctk
from .config import Config
from .layouts.RootLayout import RootLayout
from .layouts.WithSidebarLayout import WithSidebarLayout
from ..assets import AssetUtils as AssetUtils
from .stores.NavigationStore import navigation_store as navigation_store



class App(ctk.CTk):
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

    AssetUtils.prepare_assets()


  @classmethod
  def mainloop(cls) -> None:
    """Start the GUI"""

    app = App()
    Config.apply_config(app)

    # Run pre-requisites (prepare assets, etc)
    cls.prepare()

    # Render root layout
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    root = RootLayout(app)
    with_sidebar = root.set_layout(WithSidebarLayout)
    with_sidebar.active_sidebar.add_button(
      image=AssetUtils.ctk_icon("house-line"),
      command=lambda: navigation_store.navigate("dashboard")
    )
    with_sidebar.active_sidebar.add_button(
      image=AssetUtils.ctk_icon("notepad"),
      command=lambda: navigation_store.navigate("new-log")
    )

    navigation_store.navigate("dashboard")

    app.mainloop()

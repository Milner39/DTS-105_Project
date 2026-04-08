import customtkinter as _ctk
from .config import Config as _Config
from .assets import AssetUtils as _AssetUtils



class Gui:
  """Class containing methods for using the GUI"""

  @staticmethod
  def prepare():
    """
    | Run required scripts.

    | For fast start times, these scripts should be implemented in a way that they don't run from scratch every 
    execution,e.g: SVGs are only converted into PNGs if the PNG file does not already exists or is outdated.
    """

    _AssetUtils.prepare_assets()


  @staticmethod
  def mainloop():
    """Start the GUI"""

    ctk = _ctk  # Faster access in local scope


    # Run pre-requisites (prepare assets, etc)
    __class__.prepare()


    # create CTk app
    app = ctk.CTk()
    _Config.apply_config(app)

    # Configure grid (2 columns: sidebar + main content)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)


    # Sidebar frame (fixed width)
    SIDEBAR_WIDTH = 48
    sidebar = ctk.CTkFrame(app, width=SIDEBAR_WIDTH, corner_radius=0, fg_color=("gray95", "gray15"))
    sidebar.grid(row=0, column=0, sticky="ns")
    sidebar.grid_columnconfigure(0, weight=1)
    sidebar.grid_propagate(False)  # prevents resizing

    btn = ctk.CTkButton(sidebar, height=SIDEBAR_WIDTH, image=_AssetUtils.ctk_icon("house-line"), text="", corner_radius=0)
    btn.grid(row=0, column=0, sticky="ew")

    btn = ctk.CTkButton(sidebar, height=SIDEBAR_WIDTH, image=_AssetUtils.ctk_icon("notepad"), text="", corner_radius=0)
    btn.grid(row=1, column=0, sticky="ew")

    # Main content area
    main = ctk.CTkFrame(app)
    main.grid(row=0, column=1, sticky="nsew")

    app.mainloop()

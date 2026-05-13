import customtkinter as ctk
from .images.svgs import SVGUtils



class AssetUtils:
  """Class containing utilities for using assets"""

  @staticmethod
  def prepare_assets():
    """Prepare all asset files"""

    SVGUtils.prepare_icons()



  @classmethod
  def ctk_icon(cls, name: str):
    """Return a customtkinter image of the given icon"""

    icon_file = SVGUtils.get_icon(name)
    ctk_icon = ctk.CTkImage(light_image=icon_file, dark_image=icon_file)
    return ctk_icon

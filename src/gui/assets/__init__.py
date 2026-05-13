import customtkinter as ctk
from PIL import Image
from .images.svgs import SVGUtils



class AssetUtils:
  """Class containing utilities for using assets"""

  @staticmethod
  def prepare_assets():
    """Prepare all asset files"""

    SVGUtils.prepare_icons()



  @classmethod
  def ctk_icon(cls, name: str) -> ctk.CTkImage:
    """Return a customtkinter image of the given icon"""

    icon_file = SVGUtils.get_icon(name)
    return ctk.CTkImage(light_image=icon_file, dark_image=icon_file)


  @classmethod
  def ctk_icon_tinted(cls, name: str, color: tuple[int, int, int]) -> ctk.CTkImage:
    """Return a recoloured customtkinter image of the given icon"""

    source = SVGUtils.get_icon(name).convert("RGBA")
    r, g, b = color
    tinted = Image.new("RGBA", source.size, (r, g, b, 0))
    tinted.putalpha(source.split()[3])

    return ctk.CTkImage(light_image=tinted, dark_image=tinted)

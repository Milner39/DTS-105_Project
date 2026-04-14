import customtkinter as _ctk
from .images.svgs import SVGUtils as _SVGUtils



class AssetUtils:
  """Class containing utilities for using assets"""

  # Keep a reference to the loaded assets so they do not get garbage collected
  # Something is telling me this is horrible practice and will likely consume huge amounts of memory, but at least it 
  # will speed up accesses
  loaded = {
    "icons": {}
  }


  @staticmethod
  def prepare_assets():
    """Prepare all asset files"""

    _SVGUtils.prepare_icons()



  @classmethod
  def ctk_icon(cls, name: str):
    """Return a customtkinter image of the given icon"""

    loaded_icons = cls.loaded["icons"]

    # Check if icon has already been loaded
    if (name in loaded_icons and loaded_icons[name]): return loaded_icons[name]

    icon_file = _SVGUtils.get_icon(name)
    ctk_icon = _ctk.CTkImage(light_image=icon_file, dark_image=icon_file)
    cls.loaded["icons"][name] = ctk_icon
    return ctk_icon

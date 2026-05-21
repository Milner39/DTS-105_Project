import os
import resvg_py
from PIL import Image



class SVGUtils:
  """Class containing utilities for using SVG files"""

  # Define paths for icons
  SVG_DIR = os.path.join(os.path.dirname(__file__), "./")
  PNG_DIR = os.path.join(os.path.dirname(__file__), "./tmp/png-formatted/")



  @classmethod
  def prepare_icons(cls, size=256):
    """
    | Convert svg files into png files.

    | Only runs for files that are missing or outdated.
    """

    os.makedirs(cls.PNG_DIR, exist_ok=True)

    for file in os.listdir(cls.SVG_DIR):
      # Skip non-svgs
      if not file.endswith(".svg"):
        continue

      svg_path = os.path.join(cls.SVG_DIR, file)
      png_path = os.path.join(cls.PNG_DIR, file.replace(".svg", ".png"))

      # Only convert if missing or outdated
      if (
        (not os.path.exists(png_path))
        or (os.path.getmtime(svg_path) > os.path.getmtime(png_path))
      ):
        png_bytes = resvg_py.svg_to_bytes(
          svg_path=svg_path,
          width=size,
          height=size,
        )
        with open(png_path, "wb") as f:
          f.write(png_bytes)



  @classmethod
  def get_icon(cls, name: str) -> Image.Image:
    """Search for an icon of the given name and return it if found"""

    PNG_DIR = cls.PNG_DIR

    png_path = os.path.join(PNG_DIR, f"{name}.png")

    if (not os.path.exists(png_path)):
      raise FileNotFoundError(f"Icon named `{name}` does not exist")

    return Image.open(png_path)

import os as _os
import cairosvg as _cairosvg
from PIL import Image as _Image



class SVGUtils:
  """Class containing utilities for using SVG files"""

  # Define paths for icons
  SVG_DIR = _os.path.join(_os.path.dirname(__file__), "./")
  PNG_DIR = _os.path.join(_os.path.dirname(__file__), "./tmp/png-formatted/")



  @classmethod
  def prepare_icons(cls, size=64):
    """
    | Convert svg files into png files.

    | Only runs for files that are missing or outdated.
    """

    _os.makedirs(cls.PNG_DIR, exist_ok=True)

    for file in _os.listdir(cls.SVG_DIR):
      # Skip non-svgs
      if not file.endswith(".svg"):
        continue

      svg_path = _os.path.join(cls.SVG_DIR, file)
      png_path = _os.path.join(cls.PNG_DIR, file.replace(".svg", ".png"))

      # Only convert if missing or outdated
      if (
        (not _os.path.exists(png_path))
        or (_os.path.getmtime(svg_path) > _os.path.getmtime(png_path))
      ):
        _cairosvg.svg2png(
          url=svg_path,
          write_to=png_path,
          output_width=size,
          output_height=size
        )



  @classmethod
  def get_icon(cls, name: str) -> _Image.Image:
    """Search for an icon of the given name and return it if found"""

    PNG_DIR = cls.PNG_DIR

    png_path = _os.path.join(PNG_DIR, f"{name}.png")

    if (not _os.path.exists(png_path)):
      raise FileNotFoundError(f"Icon named `{name}` does not exist")

    return _Image.open(png_path)

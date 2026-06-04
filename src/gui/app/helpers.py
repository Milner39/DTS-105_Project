from collections.abc import Callable
from . import type_defs as GuiTypes



def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
  """Convert a `#RRGGBB` theme colour into an (r, g, b) tuple."""
  h = hex_color.lstrip("#")
  return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))



def bind_tree(widget: GuiTypes.CTkFrameT, sequence: str, callback: Callable):
  """Bind an event listener to the widget AND all it's children recursively."""

  widget.bind(sequence, callback, add=True)

  for child in widget.winfo_children():
    bind_tree(child, sequence, callback)

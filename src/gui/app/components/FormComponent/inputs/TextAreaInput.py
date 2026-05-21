import customtkinter as ctk
from .FormInput import FormInput
from ...TextBoxComponent import TextBoxComponent
from .... import type_defs as GuiTypes
from ....theme import Colors



class TextAreaInput(FormInput):
  """A labelled multi-line text input."""

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    label: str,
    height: int = 54,
  ):
    super().__init__(master)

    label_box = TextBoxComponent(self)
    label_box.pack(fill="x", pady=(0, 5))
    label_box.add_label(
      label,
      font=ctk.CTkFont(size=13),
      text_color=Colors.Grayscale.neutral_300,
      justify="left",
      anchor="w",
    )

    self._textbox = ctk.CTkTextbox(
      self,
      height=height,
      corner_radius=4,
      border_width=1,
      border_color=Colors.Surface.border,
      fg_color=Colors.Surface.background,
      font=ctk.CTkFont(size=12),
      wrap="word",
    )
    self._textbox.pack(fill="x")



  def get_value(self) -> str:
    """Get the text value from line 1, column 0 to the end"""
    return self._textbox.get("1.0", "end").strip()

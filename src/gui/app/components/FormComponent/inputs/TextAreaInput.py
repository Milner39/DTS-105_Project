import customtkinter as ctk
from .FormInput import FormInput
from ...TextBoxComponent import TextBoxComponent
from .... import type_defs as GuiTypes
from ....theme import Colors, Fonts, Sizes



class TextAreaInput(FormInput):
  """A labelled multi-line text input."""

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    label: str,
    lines: int = 5,
  ):
    super().__init__(master)

    label_box = TextBoxComponent(self)
    label_box.pack(fill="x")
    label_box.add_label(text=label,
      font=Fonts.Body.md(),
      text_color=Colors.Grayscale.neutral_300,
      justify="left",
      anchor="w",
    )


    # Calculate height of textbox
    textbox_font = Fonts.Body.md()
    height = (lines * textbox_font.metrics("linespace")) + (2 * Sizes.Border.md)

    self._textbox = ctk.CTkTextbox(
      self,
      height=height,
      fg_color=Colors.Surface.background,
      border_color=Colors.Surface.border,
      border_width=Sizes.Border.md,
      corner_radius=Sizes.Radius.sm,
      font=textbox_font,
      wrap="word",
    )
    self._textbox.pack(fill="x")



  def get_value(self) -> str:
    """Get the text value from line 1, column 0 to the end"""
    return self._textbox.get("1.0", "end").strip()

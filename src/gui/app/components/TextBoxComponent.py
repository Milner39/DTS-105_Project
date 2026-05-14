from .. import type_defs as GuiTypes
import customtkinter as ctk
from .FragmentComponent import FragmentComponent



class TextBoxComponent(FragmentComponent):
  """
  | A text box that automatically handles resize events.
  |
  | Useful for creating bodies of text where the text should wrap when the container shrinks.
  """

  def __init__(self, master: GuiTypes.CTkMasterT, max_width: int | None = None):
    super().__init__(master)
    self._labels: list[ctk.CTkLabel] = []
    self._max_width = max_width
    self.bind("<Configure>", self._on_resize)



  def add_label(self, text: str, **label_kwargs) -> ctk.CTkLabel:
    # Add label to the text box and list of labels to configure
    label = ctk.CTkLabel(self, text=text, justify="center", **label_kwargs)
    label.pack()
    self._labels.append(label)
    return label

  def _on_resize(self, event):
    # Set text wrap width to width to the text box or the max width if the max width is smaller
    width = min(event.width, self._max_width) if self._max_width else event.width
    for label in self._labels:
      label.configure(wraplength=width)

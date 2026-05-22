from typing import Any
import customtkinter as ctk
from ...FragmentComponent import FragmentComponent
from .... import type_defs as GuiTypes



class FormInput(FragmentComponent):
  """
  | FormInput class to extend when creating form inputs that can be registered 
    inside a the `FormComponent`.
  |
  | Child classes must implement `get_value` to return the input's current value.
  """

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self._error_label: ctk.CTkLabel | None = None


  def get_value(self) -> Any:
    raise NotImplementedError

#Error message handling for form inputs.
  def set_error(self, message: str) -> None:
    self.clear_error()
    font_obj = ctk.CTkFont(size=10)
    self._error_label = ctk.CTkLabel(
      self,
      text=message,
      font=font_obj,
      text_color="#FF5A5F",
      anchor="w",
      justify="left",
      wraplength=1,
    )
    FIXED_WRAP = 420
    self._error_label.pack(fill="x", pady=(4, 0))
    self._error_label.configure(wraplength=FIXED_WRAP)


  def clear_error(self) -> None:
    if self._error_label is not None:
      self._error_label.destroy()
      self._error_label = None

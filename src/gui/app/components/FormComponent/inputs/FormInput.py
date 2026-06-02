from collections.abc import Callable
from typing import Any
import customtkinter as ctk
from ...FragmentComponent import FragmentComponent
from ...TextBoxComponent import TextBoxComponent
from .... import type_defs as GuiTypes
from ....theme import Colors, Fonts



class FormInput(FragmentComponent):
  """
  | FormInput class to extend when creating form inputs that can be registered
    inside the `FormComponent`.
  |
  | Child classes must implement `get_value` to return the input's current value.
  | Child classes should render their widgets into `self._content` so the error
    label can be displayed below the input.
  | Child classes should call `self._on_value_change()` whenever their value
    changes so any visible error is cleared.
  """

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self._content = FragmentComponent(self)
    self._content.pack(fill="x")

    self._validators: list[Callable[[Any], str | None]] = []
    self._error_box: TextBoxComponent | None = None
    self._error_label: ctk.CTkLabel | None = None



  def get_value(self) -> Any:
    raise NotImplementedError



  def add_validator(self, fn: Callable[[Any], str | None]) -> None:
    """Add a validator. Should return an error message, or `None` if valid."""
    self._validators.append(fn)


  def validate(self) -> str | None:
    """Run validators against the current value. Return the first error or `None`."""
    value = self.get_value()
    for v in self._validators:
      err = v(value)
      if err is not None: return err
    return None



  def show_error(self, message: str | None) -> None:
    """Display validation error message. Pass in `None` to clear."""

    if message is None:
      if self._error_box is not None: self._error_box.pack_forget()
      return

    if self._error_box is None:
      self._error_box = TextBoxComponent(self)
      self._error_label = self._error_box.add_label(
        text=message,
        font=Fonts.Body.sm(),
        text_color=Colors.Semantic.error,
        justify="left",
        anchor="w",
      )
    elif self._error_label is not None:
      self._error_label.configure(text=message)

    self._error_box.pack(fill="x")



  def _on_value_change(self) -> None:
    """Call from child classes whenever the value changes to clear error."""
    self.show_error(None)

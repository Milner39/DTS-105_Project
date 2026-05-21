from typing import Any
from collections.abc import Callable
import customtkinter as ctk
from ..FragmentComponent import FragmentComponent
from ..TextBoxComponent import TextBoxComponent
from ... import type_defs as GuiTypes
from ...theme import Colors, Fonts
from .inputs import FormInput



class FormComponent(FragmentComponent):
  """
  | A form with input helpers and a submit hook.
  |
  | Use input helpers to compose the form. Inputs registered via
    `add_input` have their values collected automatically when the submit
    button is pressed and passed to the `on_submit` callback as a dict
    keyed by the names given at registration time.
  """

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    on_submit: Callable[[dict[str, Any]], None] | None = None,
  ):
    super().__init__(master)
    self._on_submit = on_submit
    self._inputs: dict[str, FormInput] = {}



  def add_heading(self, text: str) -> None:
    """Add a form heading."""
    heading_box = TextBoxComponent(self)
    heading_box.pack(fill="x", padx=22, pady=(0, 22))
    heading_box.add_label(
      text,
      font=Fonts.Heading.md(),
    )


  def add_section_heading(self, text: str) -> None:
    """Add a section sub-heading."""
    section_box = TextBoxComponent(self)
    section_box.pack(fill="x", padx=22, pady=(12, 10))
    section_box.add_label(
      text,
      font=Fonts.Heading.xs(),
      text_color=Colors.Grayscale.neutral_300,
      justify="left",
      anchor="w",
    )



  def add_input(self, name: str, field: FormInput) -> FormInput:
    """
    | Register an input as `name`.
    | It's value is collected on submit and provided in the `on_submit` 
      callback's dict under `name`.
    """
    self._inputs[name] = field
    field.pack(fill="x", padx=22, pady=(0, 14))
    return field


  def add_submit_button(self, text: str) -> None:
    """Add the submit button to a right-aligned footer."""
    footer = FragmentComponent(self)
    footer.pack(fill="x", padx=22, pady=(8, 24))

    button = ctk.CTkButton(
      footer,
      text=text,
      command=self._submit,
      fg_color=Colors.Brand.secondary,
      hover_color=Colors.Brand.secondary__dark,
      text_color=Colors.Grayscale.neutral_900,
      corner_radius=4,
      height=32,
      width=120,
      font=Fonts.Heading.xs(),
    )
    button.pack(side="right")



  def _submit(self) -> None:
    values = {name: input.get_value() for name, input in self._inputs.items()}
    if self._on_submit is not None: self._on_submit(values)

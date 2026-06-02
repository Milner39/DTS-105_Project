from typing import Any
from collections.abc import Callable
import customtkinter as ctk
from ..FragmentComponent import FragmentComponent
from ..TextBoxComponent import TextBoxComponent
from ... import type_defs as GuiTypes
from ...theme import Colors, Fonts, Sizes
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
    heading_box.pack(fill="x",
      pady=(Sizes.Spacing.none, Sizes.Spacing.md)
    )
    heading_box.add_label(text=text,
      font=Fonts.Heading.md(),
    )


  def add_section_heading(self, text: str) -> None:
    """Add a section sub-heading."""
    section_box = TextBoxComponent(self)
    section_box.pack(fill="x",
      pady=(Sizes.Spacing.md, Sizes.Spacing.none)
    )
    section_box.add_label(text=text,
      font=Fonts.Heading.xs(),
      text_color=Colors.Grayscale.neutral_300,
      justify="left",
      anchor="w",
    )



  def add_input(
    self,
    name: str,
    field: FormInput,
    validators: list[Callable[[Any], str | None]] | None = None,
  ) -> FormInput:
    """
    | Register an input as `name`.
    | It's value is collected on submit and provided in the `on_submit`
      callback's dict under `name`.
    | Optional `validators` are added to the input. On submit: each returns
      either an error message string or `None` if the value is valid.
    """
    self._inputs[name] = field
    if validators is not None:
      for v in validators: field.add_validator(v)
    field.pack(fill="x",
      pady=(Sizes.Spacing.sm, Sizes.Spacing.none)
    )
    return field


  def add_submit_button(self, text: str) -> None:
    """Add the submit button to a right-aligned footer."""
    footer = FragmentComponent(self)
    footer.pack(fill="x",
      pady=(Sizes.Spacing.lg, Sizes.Spacing.none)
    )

    button = ctk.CTkButton(footer,
      text=text,
      command=self._submit,
      fg_color=Colors.Brand.secondary,
      corner_radius=Sizes.Radius.sm,
      hover_color=Colors.Brand.secondary__dark,
      text_color=Colors.Grayscale.neutral_900,
      font=Fonts.Heading.xs(),
    )
    button.pack(side="right")



  def _submit(self) -> None:
    # Run every input's validators and show errors in the UI.
    errors = {name: input.validate() for name, input in self._inputs.items()}
    for name, input in self._inputs.items():
      input.show_error(errors[name])
    if any(err is not None for err in errors.values()): return

    values = {name: input.get_value() for name, input in self._inputs.items()}
    if self._on_submit is not None: self._on_submit(values)

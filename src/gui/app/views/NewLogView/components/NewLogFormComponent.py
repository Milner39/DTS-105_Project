from datetime import date
from typing import Any
import customtkinter as ctk
from ....components.FormComponent import FormComponent
from ....components.FormComponent.inputs import MoodScoreInput, TextAreaInput
from ....components.TextBoxComponent import TextBoxComponent
from ....theme import Colors
from .... import type_defs as GuiTypes



class NewLogFormComponent(FormComponent):
  """The mood log form: date, score, two prompts and save."""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master, on_submit=self._on_submit)

    # Add today's date above the form heading
    today = date.today()
    date_text = f"{today.strftime('%A, %B')} {today.day}, {today.year}"
    date_box = TextBoxComponent(self)
    date_box.pack(fill="x", padx=22, pady=(28, 4))
    date_box.add_label(
      date_text,
      font=ctk.CTkFont(size=12),
      text_color=Colors.Grayscale.neutral_500,
    )

    # Add the form inputs
    self.add_heading("How are you feeling today?")
    self.add_input("score", MoodScoreInput(self))
    self.add_section_heading("A couple of questions…")
    self.add_input("q1", TextAreaInput(self, label="What made you feel this way today?"))
    self.add_input("q2", TextAreaInput(self, label="Any physical symptoms? (headache, fatigue, etc.)"))
    self.add_submit_button("Save Entry")



  def _on_submit(self, values: dict[str, Any]) -> None:
    print(f"[NewLog] score={values['score']} q1={values['q1']!r} q2={values['q2']!r}")

  # Input validation
  def validate_inputs(self, values: dict[str, Any]) -> bool:
    score = values.get("score")
    q1 = values.get("q1", "").strip()
    q2 = values.get("q2", "").strip()

    is_valid = True

    # Error message for no score inputted
    if score is None:
      self.error_message(
        "score",
        "Please select a mood score between 1 and 5.",
      )
      is_valid = False

    # Error message for no answer to question 1
    if q1 == "":
      self.error_message(
        "q1",
        "Please describe what made you feel this way.",
      )
      is_valid = False

    # Error message for no answer to question 2
    if q2 == "":
      self.error_message(
        "q2",
        "Please describe any physical symptoms you are experiencing.",
      )
      is_valid = False

    return is_valid

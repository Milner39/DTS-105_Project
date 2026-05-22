from datetime import date
from typing import Any
from ....components.FormComponent import FormComponent
from ....components.FormComponent.inputs import MoodScoreInput, TextAreaInput
from ....components.TextBoxComponent import TextBoxComponent
from ....theme import Colors, Fonts
from .... import type_defs as GuiTypes



class NewLogFormComponent(FormComponent):
  """The mood log form: date, score, two prompts and save."""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master, on_submit=self._on_submit)

    # Add today's date above the form heading
    today = date.today()
    date_text = f"{today.strftime('%A, %B')} {today.day}, {today.year}"
    date_box = TextBoxComponent(self)
    date_box.pack(fill="x")
    date_box.add_label(
      date_text,
      font=Fonts.Body.md(),
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

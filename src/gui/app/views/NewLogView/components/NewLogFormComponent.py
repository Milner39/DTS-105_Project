from datetime import date
from typing import Any
import customtkinter as ctk
from ....components.FormComponent import FormComponent
from ....components.FormComponent.inputs import MoodScoreInput, TextAreaInput
from ....components.TextBoxComponent import TextBoxComponent
from ....theme import Colors
from ......database import Queries
from ......database.models.MoodLogModel import MoodLogNotesT
from .... import type_defs as GuiTypes



class NewLogFormComponent(FormComponent):
  """The mood log form: date, score, two prompts and save."""

  # Sets the form's text-area prompts
  QUESTIONS: MoodLogNotesT = [
    {
      "question": "What made you feel this way today?",
      "display": "Reasons for Score",
      "answer": "",
    },
    {
      "question": "Any physical symptoms? (headache, fatigue, etc.)",
      "display": "Physical Symptoms",
      "answer": "",
    },
  ]


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
    for i, q in enumerate(self.QUESTIONS):
      self.add_input(f"q{i}", TextAreaInput(self, label=q["question"]))
    self.add_submit_button("Save Entry")



  def _on_submit(self, values: dict[str, Any]) -> None:
    score = values["score"]
    if score is None:
      print("[NewLog] no score selected, ignoring submit")
      return

    notes: MoodLogNotesT = [
      {**q, "answer": values[f"q{i}"]} for i, q in enumerate(self.QUESTIONS)
    ]

    log = Queries.MoodLog.save_today_log(score=score, notes=notes)
    print(f"[NewLog] saved id={log.id} score={log.score} at={log.logged_at}")

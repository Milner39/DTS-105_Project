from datetime import date
from typing import Any
from ....components.FormComponent import FormComponent
from ....components.FormComponent.inputs import MoodScoreInput, TextAreaInput
from ....components.TextBoxComponent import TextBoxComponent
from ....theme import Colors, Fonts
from ......database import Queries
from ......database.models.MoodLogModel import MoodLogNotesT, MoodLogReadT
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


  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    log: MoodLogReadT | None = None,
  ):
    super().__init__(master, on_submit=self._on_submit)

    # When a log exists, drive the form from its stored notes/score so the
    # user is editing what they previously saved rather than overwriting
    # with the preset questions.
    self._notes: MoodLogNotesT = log["notes"] if log is not None else self.QUESTIONS
    initial_score: int | None = log["score"] if log is not None else None

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
    self.add_input("score", MoodScoreInput(self, initial_score=initial_score))
    self.add_section_heading("A couple of questions…")
    for i, q in enumerate(self._notes):
      self.add_input(f"q{i}", TextAreaInput(self,
        label=q["question"],
        initial_value=q["answer"],
      ))
    self.add_submit_button("Update Log" if log is not None else "Save Log")



  def _on_submit(self, values: dict[str, Any]) -> None:
    score = values["score"]
    if score is None:
      print("[NewLog] no score selected, ignoring submit")
      return

    notes: MoodLogNotesT = [
      {**q, "answer": values[f"q{i}"]} for i, q in enumerate(self._notes)
    ]

    log = Queries.MoodLog.save_today_log({"score": score, "notes": notes})
    print(f"[NewLog] saved id={log['id']} score={log['score']} at={log['logged_at']}")

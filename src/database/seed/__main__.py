"""
| Seed script: overwrite the previous calendar month with varied mood logs.
|
| Deletes every log in the previous calendar month and replaces it with a
  varied set so the app can be tested end-to-end:
  - every score (1-5) appears
  - notes are present / partial / absent
  - some days are left unlogged (gaps)
  - logged times vary across the day
"""

from datetime import date, datetime, timedelta
import random

from .. import DatabaseUtils
from ..db import db
from ..models.MoodLogModel import MoodLogModel, MoodLogNotesT



# Fixed seed so reruns reproduce the same data.
RANDOM_SEED = 105

# Roughly a fifth of days are left unlogged to create realistic gaps.
GAP_CHANCE = 0.2


# Same as `NewLogFormComponent.QUESTIONS` so seeded notes read the same.
# Kept local to avoid importing GUI code into the database module.
QUESTIONS = (
  {
    "question": "What made you feel this way today?",
    "display": "Reasons for Score",
  },
  {
    "question": "Any physical symptoms? (headache, fatigue, etc.)",
    "display": "Physical Symptoms",
  },
)


# Answer pools picked from at random to give each note some variety.
REASON_ANSWERS = (
  "Productive day, got a lot done.",
  "Caught up with friends in the evening.",
  "Slow start but finished strong.",
  "Felt a bit overwhelmed by my workload.",
  "Relaxing day off, plenty of rest.",
  "Stressful deadline at work.",
  "Good workout this morning.",
  "Quiet day, nothing much happened.",
)

SYMPTOM_ANSWERS = (
  "None.",
  "Mild headache in the afternoon.",
  "A little tired.",
  "Trouble sleeping last night.",
  "Sore from the gym.",
  "Felt great, lots of energy.",
)



def _make_notes(rng: random.Random) -> MoodLogNotesT:
  """
  | Build a `notes` list like the form's two prompts.
    - `full`          =  both answers filled
    - `reasons_only`  =  no symptoms
    - `empty`         =  no notes
  """

  shape = rng.choice(("full", "reasons_only", "empty"))

  reasons = rng.choice(REASON_ANSWERS) if shape in ("full", "reasons_only") else ""
  symptoms = rng.choice(SYMPTOM_ANSWERS) if shape == "full" else ""

  answers = (reasons, symptoms)
  notes: MoodLogNotesT = [
    {
      "question": question["question"],
      "display": question["display"],
      "answer": answer
    }
    for question, answer in zip(QUESTIONS, answers)
  ]
  return notes


def _generate_entries(
  year: int, month: int, num_days: int, rng: random.Random
) -> list[dict]:
  """Generate one log per day of the month (with gap days)."""

  entries: list[dict] = []

  # Guarantee every mood score appears by using these for the first logged days.
  forced_scores = [1, 2, 3, 4, 5]

  for day in range(1, num_days + 1):
    # Leave some days unlogged so the calendar shows gaps.
    if rng.random() < GAP_CHANCE:
      continue

    # First five logged days take scores 1..5; the rest are random.
    score = forced_scores.pop(0) if forced_scores else rng.randint(1, 5)

    logged_at = datetime(year, month, day,
      hour=rng.randint(7, 22),
      minute=rng.randint(0, 59),
    )

    entries.append({
      "logged_at": logged_at,
      "score": score,
      "notes": _make_notes(rng),
    })

  return entries


def seed_previous_month() -> None:
  """Overwrite the previous calendar month's logs with test data."""

  DatabaseUtils.prepare_database()

  # Work out the previous calendar month (rolls the year back in January).
  today = date.today()
  this_month_start = today.replace(day=1)
  prev_month_end = this_month_start - timedelta(days=1)
  prev_month_start = prev_month_end.replace(day=1)
  num_days = prev_month_end.day

  # Half-open datetime range covering the whole previous month.
  month_lo = datetime(prev_month_start.year, prev_month_start.month, 1)
  month_hi = datetime(this_month_start.year, this_month_start.month, 1)

  rng = random.Random(RANDOM_SEED)
  entries = _generate_entries(
    prev_month_start.year, prev_month_start.month, num_days, rng
  )

  # Override the previous month: clear then insert in one transaction.
  with db.atomic():
    removed = MoodLogModel.delete().where(
      (MoodLogModel.logged_at >= month_lo) & (MoodLogModel.logged_at < month_hi)
    ).execute()

    for entry in entries:
      MoodLogModel.create(**entry)

  print(
    f"[Seed]: Seeded {len(entries)} logs for "
    f"{prev_month_start.strftime('%B %Y')} (removed {removed} existing)."
  )



seed_previous_month()

from datetime import datetime
from typing import TypedDict
from peewee import Model, AutoField, DateTimeField, IntegerField
from playhouse.sqlite_ext import JSONField
from pydantic import TypeAdapter, ConfigDict, with_config
from ..db import db



# === Model Class ===

class MoodLogModel(Model):
  """The `mood log` model."""

  id = AutoField()
  logged_at = DateTimeField(default=datetime.now, null=False)
  score = IntegerField(null=False)
  notes = JSONField(null=False)

  class Meta:
    database = db
    table_name = "mood_log"

# === Model Class ===



# === Value types ===

class NoteEntryT(TypedDict):
  """One note in a MoodLog's `notes` JSON list."""
  question: str
  display: str
  answer: str

MoodLogNotesT = list[NoteEntryT]

# === Value types ===



# === CRUD schemas ===
#
#  id        : auto PK        -> READ & DELETE only
#  logged_at : system-managed -> READ only (Set on CREATE automatically)
#  score     : no default     -> Required on CREATE, optional on UPDATE
#  notes     : no default     -> Required on CREATE, optional on UPDATE
#
#  `@with_config(ConfigDict(extra="forbid"))` -> reject unknown keys
# `(TypedDict, total=False)` -> allow keys to be missing

@with_config(ConfigDict(extra="forbid"))
class MoodLogCreateT(TypedDict):
  """Fields accepted when creating a log."""
  score: int
  notes: MoodLogNotesT


@with_config(ConfigDict(extra="forbid"))
class MoodLogReadT(TypedDict):
  """All fields on a stored log."""
  id: int
  logged_at: datetime
  score: int
  notes: MoodLogNotesT


@with_config(ConfigDict(extra="forbid"))
class MoodLogUpdateT(TypedDict, total=False):
  """Fields accepted when updating a log."""
  score: int
  notes: MoodLogNotesT


@with_config(ConfigDict(extra="forbid"))
class MoodLogDeleteT(TypedDict):
  """Fields needed to delete a log."""
  id: int

# === CRUD schemas ===



# === Validators ===

MoodLogCreate = TypeAdapter(MoodLogCreateT)
MoodLogRead = TypeAdapter(MoodLogReadT)
MoodLogUpdate = TypeAdapter(MoodLogUpdateT)
MoodLogDelete = TypeAdapter(MoodLogDeleteT)

# === Validators ===

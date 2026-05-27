from datetime import date, datetime
import peewee as pw
from ..db import db
from ..models.MoodLogModel import (
  MoodLogModel,
  MoodLogNotesT,
  MoodLogCreateT,
  MoodLogUpdateT,
  MoodLogCreate,
  MoodLogUpdate,
)



class MoodLogQueries:

  @classmethod
  def save_today_log(cls, score: int, notes: MoodLogNotesT) -> MoodLogModel:
    """Upsert today's log."""

    data: MoodLogCreateT = {"score": score, "notes": notes}
    MoodLogCreate.validate_python(data, strict=True)  # runtime type safety

    now = datetime.now()
    with db.atomic():
      MoodLogModel.insert(
        logged_at = now,
        score = score,
        notes = notes,
      ).on_conflict(
        conflict_target = [pw.fn.DATE(MoodLogModel.logged_at)],
        update = {
          MoodLogModel.logged_at: now,
          MoodLogModel.score: score,
          MoodLogModel.notes: notes,
        },
      ).execute()

    log = cls.get_log_by_day(now.date())
    assert log is not None
    return log



  @classmethod
  def update_log(cls, log_id: int, data: MoodLogUpdateT) -> MoodLogModel | None:
    """Update a log with the given id."""

    clean = MoodLogUpdate.validate_python(data, strict=True)
    if not clean:
      return cls.get_log(log_id)
    MoodLogModel.update(**clean).where(MoodLogModel.id == log_id).execute()
    return cls.get_log(log_id)



  @classmethod
  def get_log(cls, log_id: int) -> MoodLogModel | None:
    """Return the log with the given id, or `None` if not found."""
    return MoodLogModel.get_or_none(MoodLogModel.id == log_id)



  @classmethod
  def get_log_by_day(cls, day: date) -> MoodLogModel | None:
    """Return the log for the given day, or `None` if not found."""
    return (MoodLogModel
      .select()
      .where(pw.fn.DATE(MoodLogModel.logged_at) == day.isoformat())
      .first()
    )



  @classmethod
  def list_logs(cls) -> list[MoodLogModel]:
    """Return all logs newest first."""
    return list(MoodLogModel.select().order_by(MoodLogModel.logged_at.desc()))



  @classmethod
  def delete_log(cls, log_id: int) -> bool:
    """Delete the log with the given id."""
    return MoodLogModel.delete().where(MoodLogModel.id == log_id).execute() > 0

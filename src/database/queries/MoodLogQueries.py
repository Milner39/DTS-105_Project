from datetime import date, datetime
import peewee as pw
from ..db import db
from ..models.MoodLogModel import (
  MoodLogModel,
  MoodLogCreateT,
  MoodLogReadT,
  MoodLogUpdateT,
  MoodLogDeleteT,
  MoodLogCreate,
  MoodLogRead,
  MoodLogUpdate,
  MoodLogDelete,
)



class MoodLogQueries:

  @classmethod
  def _to_read_dict(cls, log: MoodLogModel) -> MoodLogReadT:
    """Convert a model row into its validated read-shape dict."""
    return MoodLogRead.validate_python({
      "id": log.id,
      "logged_at": log.logged_at,
      "score": log.score,
      "notes": log.notes,
    })



  @classmethod
  def save_today_log(cls, data: MoodLogCreateT) -> MoodLogReadT:
    """Upsert today's log."""

    clean = MoodLogCreate.validate_python(data, strict=True)

    now = datetime.now()
    with db.atomic():
      MoodLogModel.insert(
        logged_at = now,
        **clean,
      ).on_conflict(
        conflict_target = [pw.fn.DATE(MoodLogModel.logged_at)],
        update = {
          MoodLogModel.logged_at: now,
          MoodLogModel.score: clean["score"],
          MoodLogModel.notes: clean["notes"],
        },
      ).execute()

    log = cls.get_log_by_day(now.date())
    assert log is not None
    return log



  @classmethod
  def update_log(cls, log_id: int, data: MoodLogUpdateT) -> MoodLogReadT | None:
    """Update a log with the given id."""

    clean = MoodLogUpdate.validate_python(data, strict=True)
    if not clean:
      return cls.get_log(log_id)
    MoodLogModel.update(**clean).where(MoodLogModel.id == log_id).execute()
    return cls.get_log(log_id)



  @classmethod
  def get_log(cls, log_id: int) -> MoodLogReadT | None:
    """Return the log with the given id, or `None` if not found."""
    log = MoodLogModel.get_or_none(MoodLogModel.id == log_id)
    return cls._to_read_dict(log) if log is not None else None



  @classmethod
  def get_log_by_day(cls, day: date) -> MoodLogReadT | None:
    """Return the log for the given day, or `None` if not found."""
    log = (MoodLogModel
      .select()
      .where(pw.fn.DATE(MoodLogModel.logged_at) == day.isoformat())
      .first()
    )
    return cls._to_read_dict(log) if log is not None else None



  @classmethod
  def list_logs(cls) -> list[MoodLogReadT]:
    """Return all logs newest first."""
    return [cls._to_read_dict(log)
      for log in MoodLogModel.select().order_by(MoodLogModel.logged_at.desc())
    ]



  @classmethod
  def delete_log(cls, data: MoodLogDeleteT) -> bool:
    """Delete the log with the given id."""
    clean = MoodLogDelete.validate_python(data, strict=True)
    return MoodLogModel.delete().where(MoodLogModel.id == clean["id"]).execute() > 0

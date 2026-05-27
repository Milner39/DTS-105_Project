from peewee import Model
from .MoodLogModel import MoodLogModel


class Models:
  MoodLog = MoodLogModel


  @classmethod
  def all(cls) -> list[type[Model]]:
    """Return every model class registered on `Models`."""
    return [
      value for value in vars(cls).values()
      if (isinstance(value, type) and issubclass(value, Model))
    ]

from . import type_defs as DBTypes
from .db import db
from .models import Models
from .queries import Queries



class DatabaseUtils:
  """Class containing utilities for using the database"""

  @staticmethod
  def prepare_database() -> None:
    """
    | Prepare the database

    - Creates the database file
    - Opens the connection
    - Creates the tables
    - Creates the day-level functional unique index
    """

    db.connect(reuse_if_open=True)             # reuse the same connection
    db.create_tables(Models.all(), safe=True)  # only create if tables do not exist

    db.execute_sql(
      "CREATE UNIQUE INDEX IF NOT EXISTS mood_log_day "
      "ON mood_log(DATE(logged_at))"
    )


  @staticmethod
  def get_connection() -> DBTypes.Database:
    """Get the connection to the database"""
    db.connect(reuse_if_open=True)
    return db

import os
from . import type_defs as DBTypes
from peewee import SqliteDatabase


"""
Define the database object.
Lets the database be created, open connections, create tables etc.
"""

_DB_PATH = os.path.join(os.path.dirname(__file__), "data.db")

db: DBTypes.Database = SqliteDatabase(_DB_PATH)

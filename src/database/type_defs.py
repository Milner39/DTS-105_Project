from typing import TypeAlias, TypeVar, TypedDict, NotRequired, Union, Tuple
import peewee


"""
Type definitions for the Database.
"""


Database: TypeAlias = peewee.SqliteDatabase

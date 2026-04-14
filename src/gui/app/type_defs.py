from typing import TypeAlias, TypeVar, TypedDict, NotRequired, Union, Tuple
import tkinter as _tk
import customtkinter as _ctk


"""
Type definitions for the GUI.

`T`  suffix: the type
`TG` suffix: the type generic
"""


CTkColorT = Union[str, Tuple[str, str]]

CTkMasterT:  TypeAlias = _tk.Misc
CTkMasterTG = TypeVar("CTkMasterTG", bound=_tk.Misc)

CTkFrameT:  TypeAlias = _ctk.CTkFrame
CTkFrameTG = TypeVar("CTkFrameTG", bound=_ctk.CTkFrame)

class CTkFrameKwargsT(TypedDict, total=False):
  width:          NotRequired[int]
  height:         NotRequired[int]
  corner_radius:  NotRequired[int]

  border_width:   NotRequired[int]
  border_color:   NotRequired[CTkColorT]

  fg_color:       NotRequired[CTkColorT]
  bg_color:       NotRequired[CTkColorT]


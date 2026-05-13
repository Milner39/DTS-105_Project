from typing import TypeAlias, TypeVar, TypedDict, NotRequired, Union, Tuple
import tkinter as tk
import customtkinter as ctk


"""
Type definitions for the GUI.

`T`  suffix: the type
`TG` suffix: the type generic
"""


CTkColorT = Union[str, Tuple[str, str]]

CTkMasterT: TypeAlias = tk.Misc
CTkMasterTG = TypeVar("CTkMasterTG", bound=tk.Misc)

CTkFrameT: TypeAlias = ctk.CTkFrame
CTkFrameTG = TypeVar("CTkFrameTG", bound=ctk.CTkFrame)

class CTkFrameKwargsT(TypedDict, total=False):
  width:          NotRequired[int]
  height:         NotRequired[int]
  corner_radius:  NotRequired[int]

  border_width:   NotRequired[int]
  border_color:   NotRequired[CTkColorT]

  fg_color:       NotRequired[CTkColorT]
  bg_color:       NotRequired[CTkColorT]


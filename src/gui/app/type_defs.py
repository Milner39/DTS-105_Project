from typing import TypeVar
import tkinter as _tk
import customtkinter as _ctk



CTkMasterT  = TypeVar("CTkMasterT", bound=_tk.Misc)
CTkFrameT   = TypeVar("CTkFrameT", bound=_ctk.CTkFrame)
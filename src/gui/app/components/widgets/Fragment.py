from typing import Unpack
from ... import type_defs as GuiTypes
import customtkinter as _ctk



class Fragment(_ctk.CTkFrame):
  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    **kwargs: Unpack[GuiTypes.CTkFrameKwargsT]
  ):
    if "fg_color" not in kwargs: kwargs.update(fg_color="transparent")

    super().__init__(master, **kwargs)

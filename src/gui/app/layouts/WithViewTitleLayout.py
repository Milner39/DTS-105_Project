import customtkinter as ctk
from . import Layout
from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes
from ..theme import Fonts



class WithViewTitleLayout(Layout):
  """Title and content layout"""

  def __init__(self, master: GuiTypes.CTkMasterT, title_text: str = ""):
    super().__init__(master)

    self._title_area:   GuiTypes.CTkFrameT
    self._content_area:   GuiTypes.CTkFrameT


    self.grid(row=0, column=0, sticky="nsew")
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=0)
    self.grid_rowconfigure(1, weight=1)


    title_area = FragmentComponent(self)
    title_area.grid(row=0, column=0, sticky="ew")
    title_area.grid_rowconfigure(0, weight=1)
    title_area.grid_columnconfigure(0, weight=1)
    self._title_area = title_area

    title = ctk.CTkLabel(title_area,
      text=title_text,
      font=Fonts.Heading.lg()
    )
    title.pack(padx=8, pady=8)
    self.title = title


    content_area = FragmentComponent(self)
    content_area.grid(row=1, column=0, sticky="nsew")
    content_area.grid_rowconfigure(0, weight=1)
    content_area.grid_columnconfigure(0, weight=1)
    self._content_area = content_area



  def set_content(self, new_content: type[GuiTypes.CTkFrameTG], *args, **kwargs) -> GuiTypes.CTkFrameTG:
    content = super().set_content(new_content, self._content_area, *args, **kwargs)

    content.grid(row=0, column=0, sticky="nsew")

    return content

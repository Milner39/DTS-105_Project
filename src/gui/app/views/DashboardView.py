import customtkinter as ctk
from ..components.FragmentComponent import FragmentComponent
from ..components.TextBoxComponent import TextBoxComponent
from ..layouts.WithViewTitleLayout import WithViewTitleLayout
from .. import type_defs as GuiTypes
from ...assets import AssetUtils



class DashboardView(FragmentComponent):
  """The `home` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)


    view_title_layout = WithViewTitleLayout(self, "Home")
    content = view_title_layout.set_content(FragmentComponent)


    center = FragmentComponent(content)
    center.pack(expand=True, fill="x")

    text_box = TextBoxComponent(center)
    text_box.pack(fill="x", padx=16)
    text_box.add_label("Welcome to MoodMinder", font=ctk.CTkFont(size=20, weight="bold"))
    text_box.add_label("Track your mood and wellbeing, one log at a time.", font=ctk.CTkFont(size=16))

    logo_label = ctk.CTkLabel(center, text="", image=AssetUtils.ctk_icon("moodminder-logo", 128))
    logo_label.pack(padx=16, pady=16)

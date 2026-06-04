from datetime import date
import customtkinter as ctk

from ....components.FragmentComponent import FragmentComponent
from ....components.ScoreCircleComponent import ScoreCircleComponent
from ....components.TextBoxComponent import TextBoxComponent
from ....theme import Colors, Fonts, Sizes
from .... import type_defs as GuiTypes
from ......database.models.MoodLogModel import MoodLogReadT
from .....assets import AssetUtils
from ....helpers import hex_to_rgb



class SelectedLogComponent(FragmentComponent):
  """
  | The selected-day detail panel:
    - score
    - note
    - edit / delete actions
  """

  MOOD_LABELS = ("Very Low", "Low", "Okay", "Good", "Great")
  ICON_SIZE = Sizes.Dimension.xs


  def __init__(self,
    master: GuiTypes.CTkMasterT,
    *,
    on_edit,
    on_delete,
  ):
    super().__init__(master)
    self._on_edit = on_edit
    self._on_delete = on_delete



  def render(self,
    day: date | None,
    log: MoodLogReadT | None
  ) -> None:
    """Render the component."""

    # Destroy the last draw
    for child in self.winfo_children():
      child.destroy()


    # Show a placeholder when no day is selected
    if day is None:
      ctk.CTkLabel(self,
        text="Select a day",
        font=Fonts.Heading.xs(),
        text_color=Colors.Grayscale.neutral_500, 
        anchor="w"
      ).pack(fill="x")
      return



    # Create the date heading
    ctk.CTkLabel(self,
      text=day.strftime("%a, %b ") + str(day.day),
      font=Fonts.Heading.xs(),
      anchor="w"
    ).pack(fill="x")


    # Show a message when the day has no log
    if log is None:
      ctk.CTkLabel(self,
        text="No log for this day.",
        font=Fonts.Body.md(),
        text_color=Colors.Grayscale.neutral_500,
        anchor="w"
      ).pack(fill="x", pady=(Sizes.Spacing.sm, 0))
      return



    # == Show log data ==

    # Create the container for log info
    head = FragmentComponent(self)
    head.pack(fill="x", pady=(Sizes.Spacing.sm, 0))

    # Show the score circle
    ScoreCircleComponent(head,
      log["score"],
      size=Sizes.Dimension.sm,
    ).pack(side="left")

    # Create the container for the mood label and log time
    info = FragmentComponent(head)
    info.pack(side="left", fill="x", expand=True, padx=(Sizes.Spacing.sm, 0))

    # Show mood label
    ctk.CTkLabel(info,
      text=self.MOOD_LABELS[max(1, min(5, log["score"])) - 1],
      font=Fonts.Body.md(),
      text_color=Colors.Grayscale.neutral_300,
      anchor="w"
    ).pack(fill="x")

    # Show log time
    ctk.CTkLabel(info,
      text="logged " + log["logged_at"].strftime("%I:%M %p").lstrip("0"),
      font=Fonts.Body.sm(),
      text_color=Colors.Grayscale.neutral_500,
      anchor="w"
    ).pack(fill="x")

    # Show the first note answer if one exists
    notes = log["notes"]
    note = notes[0]["answer"] if notes else ""
    if note:
      note_box = FragmentComponent(self,
        border_width=Sizes.Border.sm,
        border_color=Colors.Surface.border,
        corner_radius=Sizes.Radius.sm
      )
      note_box.pack(fill="x", pady=(Sizes.Spacing.sm, 0))
      text_box = TextBoxComponent(note_box)
      text_box.pack(fill="x", padx=Sizes.Spacing.sm, pady=Sizes.Spacing.sm)
      text_box.add_label(f'"{note}"',
        font=Fonts.Body.sm(),
        text_color=Colors.Grayscale.neutral_300,
        justify="left",
        anchor="w"
      )


    # == Create the edit & delete buttons ==

    # Create the grid to hold the action buttons
    actions = FragmentComponent(self)
    actions.pack(fill="x", pady=(Sizes.Spacing.sm, 0))
    actions.grid_columnconfigure(0, weight=1)
    actions.grid_columnconfigure(1, weight=1)

    # Show edit button
    edit_btn = ctk.CTkButton(actions,
      text="Edit",
      image=AssetUtils.ctk_icon_tinted("pencil-simple",
        hex_to_rgb(Colors.Grayscale.neutral_300), self.ICON_SIZE
      ),
      font=Fonts.Body.md(),
      fg_color="transparent",
      border_width=Sizes.Border.sm,
      border_color=Colors.Surface.border,
      text_color=Colors.Grayscale.neutral_300,
      hover_color=Colors.Grayscale.neutral_700,
      corner_radius=Sizes.Radius.sm,
      command=self._on_edit,
    )
    edit_btn.grid(row=0, column=0, sticky="ew", padx=(0, Sizes.Spacing.xs))

    # DShow delete button
    delete_btn = ctk.CTkButton(actions,
      text="Delete",
      image=AssetUtils.ctk_icon_tinted("trash",
        hex_to_rgb(Colors.Semantic.error), self.ICON_SIZE
      ),
      font=Fonts.Body.md(),
      fg_color="transparent",
      border_width=Sizes.Border.sm,
      border_color=Colors.Semantic.error,
      text_color=Colors.Semantic.error,
      hover_color=Colors.Grayscale.neutral_700,
      corner_radius=Sizes.Radius.sm,
      command=self._on_delete,
    )
    delete_btn.grid(row=0, column=1, sticky="ew", padx=(Sizes.Spacing.xs, 0))

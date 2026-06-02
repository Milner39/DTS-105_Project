import customtkinter as ctk
from ...FragmentComponent import FragmentComponent
from .FormInput import FormInput
from typing import Any
from collections.abc import Callable
from .... import type_defs as GuiTypes
from ....theme import Colors, Fonts, Sizes



def bind_tree(widget: GuiTypes.CTkFrameT, sequence: str, callback: Callable):
  """Bind an event listener to the widget AND all it's children recursively."""

  widget.bind(sequence, callback, add=True)

  for child in widget.winfo_children():
    bind_tree(child, sequence, callback)



class MoodScoreInput(FormInput):
  """Row of 5 selectable tiles (1-5) for picking a mood score."""

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    on_change: Callable[[int], Any] | None = None,
    initial_score: int | None = None,
  ):
    super().__init__(master)

    self.LABELS = ("Very Low", "Low", "Okay", "Good", "Great")

    self._on_change = on_change
    self._score: int | None = None
    self._tiles: list[dict] = []

    self._create_tiles()

    if initial_score is not None:
      self._score = initial_score
      self._restyle()



  def _create_tiles(self) -> None:
    """Create the tiles."""

    for tile_index in range(len(self.LABELS)):
      tile_num = tile_index+1
      tile_column = tile_index * 2

      # Tile column: equal width with the other tile columns due to the `uniform` arg.
      self._content.grid_columnconfigure(tile_column, weight=1, uniform="tile")

      # Spacer column between this tile and the previous one (skip for first).
      if tile_index > 0:
        self._content.grid_columnconfigure(tile_column - 1,
          weight=0, minsize=Sizes.Spacing.sm
        )


      # Create the widgets for the tile
      tile = FragmentComponent(self._content,
        border_width=Sizes.Border.sm,
        border_color=Colors.Surface.border,
      )
      tile.grid(row=0, column=tile_column, sticky="ew")
      tile.grid_rowconfigure(0, weight=0)
      tile.grid_rowconfigure(1, weight=0)
      tile.grid_columnconfigure(0, weight=1)

      number = ctk.CTkLabel(tile,
        text=str(tile_num),
        font=Fonts.Heading.xl(),
        text_color=Colors.Grayscale.neutral_300,
      )
      number.grid(row=0, column=0,
        pady=(Sizes.Spacing.sm, Sizes.Spacing.none)
      )

      label = ctk.CTkLabel(tile,
        text=self.LABELS[tile_index],
        font=Fonts.Body.sm(),
        text_color=Colors.Grayscale.neutral_300,
      )
      label.grid(row=1, column=0,
        pady=(Sizes.Spacing.none, Sizes.Spacing.sm)
      )


      # Bind a click event listener to tile
      on_click = lambda _e, score=tile_num: self._select(score)
      bind_tree(tile, "<Button-1>", on_click)

      # Add tile to the tiles list
      self._tiles.append({"tile": tile, "number": number, "label": label})



  def _select(self, score: int) -> None:
    """
      - Set score
      - Restyle tiles
      - Clear validation error
      - Notify listener
    """
    self._score = score
    self._restyle()
    self._on_value_change()
    if self._on_change is not None: self._on_change(score)


  def _restyle(self) -> None:
    """Apply the selected / unselected styling to each tile based on the current score."""

    for tile_index, parts in enumerate(self._tiles):
      tile_num = tile_index+1

      is_selected = tile_num == self._score

      if is_selected:
        # Highlight the selected tile
        parts["tile"].configure(
          border_width=Sizes.Border.md,
          border_color=Colors.Brand.secondary,
          fg_color=Colors.Brand.secondary__transparent,
        )
        parts["number"].configure(text_color=Colors.Brand.secondary)
        parts["label"].configure(text_color=Colors.Brand.secondary)
      else:
        # Reset every other tile to the default appearance
        parts["tile"].configure(
          border_width=Sizes.Border.sm,
          border_color=Colors.Surface.border,
          fg_color="transparent",
        )
        parts["number"].configure(text_color=Colors.Grayscale.neutral_300)
        parts["label"].configure(text_color=Colors.Grayscale.neutral_300)



  def get_value(self) -> int | None:
    return self._score

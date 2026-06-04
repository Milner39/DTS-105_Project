from __future__ import annotations

import tkinter as tk
from tkinter import Event, Canvas
from .. import type_defs as GuiTypes
from ..theme import Colors, Sizes
from .FragmentComponent import FragmentComponent



class LineGraphComponent(FragmentComponent):
  """
  | A small line graph of mood scores (1-5) over time, drawn on a Canvas.
  |
  | Renders dashed gridlines for each score, a filled area under the line, and
    point markers.
  """

  def __init__(self,
    master: GuiTypes.CTkMasterT,
    data: list[int] | None = None,
    height: int = Sizes.Dimension.lg,
    bg_color: str = Colors.Surface.background,
  ):
    super().__init__(master)

    self._data: list[int] = data if data is not None else []
    """The points to plot."""

    self._height = height
    """The height of the chart."""

    self._padding = {
      "t": Sizes.Spacing.sm,
      "r": Sizes.Spacing.sm,
      "b": Sizes.Spacing.sm,
      "l": Sizes.Dimension.xs,
    }
    """The padding around the chart in the canvas."""


    # Create the canvas and bind a resize listener to run the `_redraw` method.
    self._canvas = tk.Canvas(self,
      height=height,
      highlightthickness=0,
      bd=0,
      bg=bg_color,
    )
    self._canvas.pack(fill="x")
    self._canvas.bind("<Configure>", self._redraw)



  def set_data(self, data: list[int]) -> None:
    """Replace the plotted data and redraw."""
    self._data = data
    self._redraw()



  def _redraw(self, event: Event[Canvas] | None = None) -> None:
    """Draw the chart on the canvas."""

    c = self._canvas
    d = self._data

    n_points = len(d)
    """The number of data points."""


    # Clear the canvas
    c.delete("all")



    # Get dimensions of widget
    width = event.width if event is not None else c.winfo_width()
    height = self._height
    if width <= 1:
      return

    # Calculate dimensions of the data area of the graph
    pad = self._padding
    plot_w = width - pad["l"] - pad["r"]
    plot_h = height - pad["t"] - pad["b"]



    def y_for_score(score: float) -> float:
      """Get the y coordinate on the chart for the given score."""
      return pad["t"] + plot_h - ((score - 1) / 4) * plot_h


    def x_for_point(i: int) -> float:
      """Get the x coordinate on the chart for the given index of point"""
      if n_points == 1:
        # Prevent divide by zero error
        return pad["l"] + plot_w / 2

      return pad["l"] + (i / (n_points - 1)) * plot_w



    # Draw grid lines and y-axis score labels
    for s in range(1, 6):
      y = y_for_score(s)
      c.create_line(
        pad["l"],           # x0
        y,                  # y0
        pad["l"] + plot_w,  # x1
        y,                  # y1
        fill=Colors.Surface.border,
        dash=(3, 2)
      )
      c.create_text(
        pad["l"] - Sizes.Spacing.xs,  # x
        y,                            # y
        text=str(s),
        anchor="e",
        fill=Colors.Grayscale.neutral_500,
        font=("", 8)
      )



    # Return early if no data given
    if d is None:
      c.create_text(
        width / 2,   # x
        height / 2,  # y
        text="No data",
        fill=Colors.Grayscale.neutral_700,
        font=("", 10)
      )
      return


    # Get coordinates of all points
    points = [(x_for_point(i), y_for_score(v)) for i, v in enumerate(d)]

    # Don't draw line of line graph if only 1 point exists
    if n_points > 1:
      # == Filled area under the line ==

      # Create polygon coordinates list.
      area: list[tuple[float, float]] = [(
        pad["l"],          # x
        pad["t"] + plot_h  # y
      )]
      # Starts with the bottom left corner of the graph

      # Add data coordinates to the polygon area
      area.extend(points)

      # Add bottom right corner
      area.append((
        points[-1][0],     # x
        pad["t"] + plot_h  # y
      ))

      # Draw
      c.create_polygon(area,
        fill=Colors.Brand.secondary__transparent,
        outline=""
      )


      # == The line ==

      # Draw
      c.create_line(points,
        fill=Colors.Brand.secondary,
        width=Sizes.Border.md,
        joinstyle="round"
      )


    # == Point markers ==

    # radius of point markers
    r = 3

    for (x, y) in points:
      # Draw
      c.create_oval(
        x - r,  # x0
        y - r,  # y0
        x + r,  # x1
        y + r,  # y1
        fill=Colors.Brand.secondary,
        outline=Colors.Surface.background,
        width=1
      )

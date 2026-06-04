from datetime import date
import customtkinter as ctk

from ....components.FragmentComponent import FragmentComponent
from ....theme import Colors, Fonts, Sizes
from .... import type_defs as GuiTypes
from .....assets import AssetUtils
from ....helpers import hex_to_rgb



class MonthNavComponent(FragmentComponent):
  """
  | Month switcher row:
    - previous month button
    - month and year label
    - next month button
    - 'Log Today' button
  """

  ICON_SIZE = Sizes.Dimension.xs


  def __init__(self,
    master: GuiTypes.CTkMasterT,
    *,
    on_prev,
    on_next,
    on_log_today,
  ):
    # Init self and set up the layout grid
    super().__init__(master, height=Sizes.Dimension.md)
    self.grid_propagate(False)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=0)
    self.grid_columnconfigure(2, weight=0)
    self.grid_columnconfigure(3, weight=1)  # spacer pushes 'Log Today' button right
    self.grid_columnconfigure(4, weight=0)


    # Create the previous month button
    prev_btn = ctk.CTkButton(self,
      text="",
      width=Sizes.Dimension.sm,
      image=AssetUtils.ctk_icon_tinted("caret-left",
        hex_to_rgb(Colors.Grayscale.neutral_300), self.ICON_SIZE
      ),
      fg_color="transparent",
      hover_color=Colors.Grayscale.neutral_700,
      command=on_prev,
    )
    prev_btn.grid(row=0, column=0)

    # Create the month and year label
    self._month_label = ctk.CTkLabel(self,
      text="",
      font=Fonts.Heading.sm()
    )
    self._month_label.grid(row=0, column=1, padx=Sizes.Spacing.sm)

    # Create the next month button
    next_btn = ctk.CTkButton(self,
      text="",
      width=Sizes.Dimension.sm,
      image=AssetUtils.ctk_icon_tinted("caret-right",
        hex_to_rgb(Colors.Grayscale.neutral_300), self.ICON_SIZE
      ),
      fg_color="transparent",
      hover_color=Colors.Grayscale.neutral_700,
      command=on_next,
    )
    next_btn.grid(row=0, column=2)

    # Create the 'Log Today' button
    log_today_btn = ctk.CTkButton(self,
      text="Log Today",
      image=AssetUtils.ctk_icon_tinted("plus",
        hex_to_rgb(Colors.Grayscale.neutral_900), self.ICON_SIZE
      ),
      fg_color=Colors.Brand.secondary,
      hover_color=Colors.Brand.secondary__dark,
      text_color=Colors.Grayscale.neutral_900,
      font=Fonts.Heading.xs(),
      corner_radius=Sizes.Radius.sm,
      command=on_log_today,
    )
    log_today_btn.grid(row=0, column=4)



  def set_month(self, month: date) -> None:
    """Update the displayed month label."""
    self._month_label.configure(text=month.strftime("%B %Y"))

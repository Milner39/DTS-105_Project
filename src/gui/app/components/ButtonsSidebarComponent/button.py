import customtkinter as ctk
from collections.abc import Callable
from ... import type_defs as GuiTypes
from ...theme import Colors



class Button(ctk.CTkButton):
  """Styled button for sidebar"""

  def __init__(
    self,
    master: GuiTypes.CTkMasterT,
    *,
    height: int,
    image : ctk.CTkImage,
    active_image: ctk.CTkImage,
    command: Callable | None
  ):
    super().__init__(
      master=master,
      height=height,
      text="",
      command=command,
      image=image,
      corner_radius=0,
      fg_color="transparent",
      hover_color=Colors.Grayscale.neutral_700,
      anchor="center",
    )
    self._image_normal = image
    self._image_active = active_image


  def set_active(self, is_active: bool) -> None:
    self.configure(
      fg_color=Colors.Brand.secondary if is_active else "transparent",
      hover=not is_active,
      image=self._image_active if is_active else self._image_normal,
    )

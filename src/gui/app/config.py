import customtkinter as _ctk



class Config:
  """Class containing methods for the configuration of the customtkinter app"""

  ctk = _ctk  # Faster access in local scope


  @staticmethod
  def apply_config(app: _ctk.CTk) -> None:
    """Apply configuration defaults to customtkinter app"""

    # Apply config
    __class__.ctk.set_appearance_mode("system")
    __class__.ctk.set_default_color_theme("blue")
    __class__.ctk.set_window_scaling(1.0)
    __class__.ctk.set_widget_scaling(1.0)
    app.geometry("854x480")

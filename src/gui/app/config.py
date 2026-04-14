import customtkinter as _ctk



class Config:
  """Class containing methods for the configuration of the customtkinter app"""

  @classmethod
  def apply_config(cls, app: _ctk.CTk) -> None:
    """Apply configuration defaults to customtkinter app"""

    # Apply config
    _ctk.set_appearance_mode("system")
    _ctk.set_default_color_theme("blue")
    _ctk.set_window_scaling(1.0)
    _ctk.set_widget_scaling(1.0)
    app.geometry("854x480")

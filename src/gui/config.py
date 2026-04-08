import customtkinter as _ctk



class Config:
  """Class containing methods for the configuration of the customtkinter app"""

  @staticmethod
  def apply_config(app: _ctk.CTk) -> None:
    """Apply configuration defaults to customtkinter app"""

    ctk = _ctk  # Faster access in local scope

    # Apply config
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    ctk.set_window_scaling(1.0)
    ctk.set_widget_scaling(1.0)
    app.geometry("854x480")

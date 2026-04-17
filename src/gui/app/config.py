import customtkinter as ctk



class Config:
  """Class containing methods for the configuration of the customtkinter app"""

  @classmethod
  def apply_config(cls, app: ctk.CTk) -> None:
    """Apply configuration defaults to customtkinter app"""

    # Apply config
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    ctk.set_window_scaling(1.0)
    ctk.set_widget_scaling(1.0)
    app.geometry("854x480")

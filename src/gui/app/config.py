import customtkinter as ctk



class Config:
  """Class containing methods for the configuration of the customtkinter app"""

  @classmethod
  def apply_config(cls, app: ctk.CTk) -> None:
    """Apply configuration to customtkinter app"""

    # Apply config
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    ctk.set_window_scaling(1.0)
    ctk.set_widget_scaling(1.0)
    ctk.DrawEngine.preferred_drawing_method = "circle_shapes"
    app.geometry("1280x720")
    app.title("MoodMinder")

import customtkinter as ctk


class _Heading:
  @staticmethod
  def xs() -> ctk.CTkFont: return ctk.CTkFont(size=14, weight="bold")

  @staticmethod
  def sm() -> ctk.CTkFont: return ctk.CTkFont(size=20, weight="bold")

  @staticmethod
  def md() -> ctk.CTkFont: return ctk.CTkFont(size=22, weight="bold")

  @staticmethod
  def lg() -> ctk.CTkFont: return ctk.CTkFont(size=24, weight="bold")

  @staticmethod
  def xl() -> ctk.CTkFont: return ctk.CTkFont(size=26, weight="bold")

class _Body:
  @staticmethod
  def sm() -> ctk.CTkFont: return ctk.CTkFont(size=10)

  @staticmethod
  def md() -> ctk.CTkFont: return ctk.CTkFont(size=12)

  @staticmethod
  def lg() -> ctk.CTkFont: return ctk.CTkFont(size=16)



class Fonts:
  """Single source of truth for every font used in the GUI."""
  Heading = _Heading
  Body    = _Body

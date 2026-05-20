from .type_defs import CTkColorT



class _Brand:
  primary_100:  CTkColorT = "#8D62F2"
  primary_300:  CTkColorT = "#E064C7"
  primary_500:  CTkColorT = "#FF7B84"
  primary_700:  CTkColorT = "#FF8D46"
  primary_900:  CTkColorT = "#F2E662"

  secondary:        CTkColorT = "#009994"
  secondary__light: CTkColorT = "#00CCC5"
  secondary__dark:  CTkColorT = "#006663"



class _Grayscale:
  neutral_100:  CTkColorT = "#00100B"
  neutral_300:  CTkColorT = "#3A4743"
  neutral_500:  CTkColorT = "#747F7B"
  neutral_700:  CTkColorT = "#AEB6B3"
  neutral_900:  CTkColorT = "#E8EDEB"



class _Surface:
  background:  CTkColorT = _Grayscale.neutral_900
  border:      CTkColorT = _Grayscale.neutral_700



class Colors:
  """Single source of truth for every colour used in the GUI."""
  Brand     = _Brand
  Grayscale = _Grayscale
  Surface   = _Surface

from ..type_defs import CTkColorT

# Light / Dark variants use HSL colour space and have their lightness +/- by 10%
# Transparent variants are pre-blended against a white background at 20% opacity

class _Brand:
  primary_100:  CTkColorT = "#8D62F2"
  primary_300:  CTkColorT = "#E064C7"
  primary_500:  CTkColorT = "#FF7B84"
  primary_700:  CTkColorT = "#FF8D46"
  primary_900:  CTkColorT = "#F2E662"

  secondary:        CTkColorT = "#009994"
  secondary__light: CTkColorT = "#00CCC5"
  secondary__dark:  CTkColorT = "#006663"
  secondary__transparent: CTkColorT = "#CCEBEA"


class _Grayscale:
  neutral_100:  CTkColorT = "#00100B"
  neutral_300:  CTkColorT = "#3A4743"
  neutral_500:  CTkColorT = "#747F7B"
  neutral_700:  CTkColorT = "#AEB6B3"
  neutral_900:  CTkColorT = "#E8EDEB"



class _Surface:
  background:  CTkColorT = _Grayscale.neutral_900
  border:      CTkColorT = _Grayscale.neutral_700



class _Semantic:
  error:  CTkColorT = "#E84A4A"



class _Mood:
  """Mood-score colour scale (1-5), drawn from the brand primary spectrum."""
  score_1:  CTkColorT = _Brand.primary_100
  score_2:  CTkColorT = _Brand.primary_300
  score_3:  CTkColorT = _Brand.primary_500
  score_4:  CTkColorT = _Brand.primary_700
  score_5:  CTkColorT = _Brand.primary_900

  @classmethod
  def for_score(cls, score: int) -> CTkColorT:
    """Return the colour for a 1-5 mood score."""
    scale = (cls.score_1, cls.score_2, cls.score_3, cls.score_4, cls.score_5)
    return scale[max(1, min(5, score)) - 1]



class Colors:
  """Single source of truth for every colour used in the GUI."""
  Brand     = _Brand
  Grayscale = _Grayscale
  Surface   = _Surface
  Semantic  = _Semantic
  Mood      = _Mood

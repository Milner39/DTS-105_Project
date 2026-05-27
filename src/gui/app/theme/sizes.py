class _Spacing:
  """Padding and gap values."""
  none: int = 0
  xs:   int = 4
  sm:   int = 8
  md:   int = 16
  lg:   int = 24
  xl:   int = 32


class _Radius:
  """Corner-radius values."""
  none: int = 0
  sm:   int = 4
  lg:   int = 8


class _Border:
  """Border-width values."""
  none: int = 0
  sm: int = 1
  md: int = 2
  lg: int = 4


class _Dimension:
  """Large fixed pixel dimensions for icons, sidebars, etc"""
  none: int = 0
  xs: int = 16
  sm: int = 32
  md: int = 48
  lg: int = 64
  xl: int = 96
  xxl: int = 128



class Sizes:
  """Single source of truth for every numeric size used in the GUI."""
  Spacing   = _Spacing
  Radius    = _Radius
  Border    = _Border
  Dimension = _Dimension

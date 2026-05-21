from typing import Any
from ...FragmentComponent import FragmentComponent



class FormInput(FragmentComponent):
  """
  | FormInput class to extend when creating form inputs that can be registered 
    inside a the `FormComponent`.
  |
  | Child classes must implement `get_value` to return the input's current value.
  """

  def get_value(self) -> Any:
    raise NotImplementedError

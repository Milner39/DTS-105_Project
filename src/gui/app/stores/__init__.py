from copy import deepcopy
from collections.abc import Callable
from typing import Generic, TypeAlias, TypeVar

StateTG = TypeVar("StateTG")

SubscriberT: TypeAlias = Callable[[StateTG, StateTG], None]
SubscriberSetT: TypeAlias = set[SubscriberT[StateTG]]



class Store(Generic[StateTG]):
  """
  | Store class to extend when creating real stores.
  |
  | A type can be passed in when inheriting from this class to type the derived store's state.
  |
  | Stores inheriting from this class should mutate state by creating methods that use...
  | `set_state`: Completely replace the current state
  | `patch_state`: Provide a callback that takes a deep-copy of the current state, modifies it, then returns it
  | `reset_state`: Completely replace the current state with `_initial_state`
  |
  | This has been implemented this way to prevent accidentally modifying `_state` directly by using deep-copies.
  """

  def __init__(self, initial_state: StateTG):
    self._initial_state: StateTG = deepcopy(initial_state)
    self._state: StateTG = deepcopy(initial_state)
    self._subscribers: SubscriberSetT[StateTG] = set()



  def get_state(self) -> StateTG:
    """Returns a deep copy of current state."""
    return deepcopy(self._state)

  def set_state(self, next_state: StateTG) -> None:
    """Sets a deep copy of given state"""
    prev = self.get_state()
    self._state = deepcopy(next_state)
    self._notify(prev)

  def patch_state(self, patcher: Callable[[StateTG], StateTG]) -> None:
    """
    | Sets the state returned from a callback function that modifies 
      the current state.
    """
    self.set_state(patcher(self.get_state()))

  def reset_state(self) -> None:
    """Resets the state to the initial state."""
    self.set_state(self._initial_state)


  def subscribe(self, callback: SubscriberT[StateTG]) -> Callable[[], None]:
    """
    | Lets other areas of the codebase run a callback whenever 
      the state changes.
    """

    self._subscribers.add(callback)

    def unsubscribe() -> None:
      self._subscribers.discard(callback)

    return unsubscribe

  def _notify(self, prev: StateTG) -> None:
    """Broadcasts the current and previous state to all subscribers."""
    for subscriber in self._subscribers:
      subscriber(self.get_state(), prev)

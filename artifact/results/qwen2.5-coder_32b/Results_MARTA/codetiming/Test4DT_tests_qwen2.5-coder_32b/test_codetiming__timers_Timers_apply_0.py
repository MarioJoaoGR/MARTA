
import pytest
from typing import List, Callable
from collections import defaultdict
from codetiming._timers import Timers

class Timers:
    """
    Custom dictionary that stores information about timers.
    """

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        self._timings: defaultdict[str, list[float]] = defaultdict(list)

    def add(self, name: str, value: float) -> None:
        """Add a timing entry for the specified timer."""
        self._timings[name].append(value)

    def apply(self, func: Callable[[List[float]], float], name: str) -> float:
        """
        Applies a given function to the list of recorded times for a specified timer.
        """
        if name in self._timings:
            return func(self._timings[name])
        raise KeyError(name)


def test_apply_with_sum():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    result = timers.apply(sum, 'example_timer')
    assert result == 4.6

def test_apply_with_max():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    result = timers.apply(max, 'example_timer')
    assert result == 3.4

def test_apply_with_min():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    result = timers.apply(min, 'example_timer')
    assert result == 1.2

def test_apply_with_lambda():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    result = timers.apply(lambda values: sum(values) / len(values), 'example_timer')
    assert result == 2.3

def test_apply_with_missing_key():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(sum, 'non_existent_timer')

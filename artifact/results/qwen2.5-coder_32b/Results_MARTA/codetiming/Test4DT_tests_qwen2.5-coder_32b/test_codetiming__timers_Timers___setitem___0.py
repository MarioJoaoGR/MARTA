
import pytest
from collections import defaultdict
from codetiming._timers import Timers

class Timers:
    """
    Custom dictionary that stores information about timers.
    """

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        self._timings: defaultdict[str, list[float]] = defaultdict(list)

    def __setitem__(self, name: str, value: float) -> None:
        """Disallow setting of timer values"""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support item assignment. "
        )

def test_valid_case():
    timers = Timers()
    with pytest.raises(TypeError):
        timers['load_data'] = 0.5

def test_edge_cases():
    timers = Timers()
    # Test with None
    with pytest.raises(TypeError):
        timers[None] = 0.5  # type: ignore
    # Test with empty string
    with pytest.raises(TypeError):
        timers[''] = 0.5
    # Test with boundary values for name (e.g., single character)
    with pytest.raises(TypeError):
        timers['a'] = 0.5
    # Test with boundary values for value (e.g., zero, negative, positive)
    with pytest.raises(TypeError):
        timers['load_data'] = 0.0
    with pytest.raises(TypeError):
        timers['load_data'] = -0.1
    with pytest.raises(TypeError):
        timers['load_data'] = 0.1

def test_invalid_inputs():
    timers = Timers()
    # Test with non-string names
    with pytest.raises(TypeError):
        timers[123] = 0.5  # type: ignore
    with pytest.raises(TypeError):
        timers[None] = 0.5  # type: ignore
    # Test with non-float values
    with pytest.raises(TypeError):
        timers['load_data'] = '0.5'  # type: ignore
    with pytest.raises(TypeError):
        timers['load_data'] = [0.5]  # type: ignore


import pytest
from collections import defaultdict

class Timers:
    """
    Custom dictionary that stores information about timers.
    """

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        self._timings: Dict[str, List[float]] = defaultdict(list)

    def __setitem__(self, name: str, value: float) -> None:
        """Disallow setting of timer values"""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support item assignment. "
        )

def test_valid_case():
    timers = Timers()
    with pytest.raises(TypeError):
        timers['some_timer'] = 0.5

def test_edge_case_none_name():
    timers = Timers()
    with pytest.raises(TypeError):
        timers[None] = 0.5

def test_invalid_input_non_string_name():
    timers = Timers()
    with pytest.raises(TypeError):
        timers[123] = 0.5

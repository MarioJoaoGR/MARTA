
import pytest
from typing import List, Dict, Callable, Any
import collections

class Timers:
    """Custom dictionary that stores information about timers."""
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Timer instance and set up a private dictionary to keep track of all timings."""
        super().__init__(*args, **kwargs)
        self._timings: Dict[str, List[float]] = collections.defaultdict(list)

    def apply(self, func: Callable[[List[float]], float], name: str) -> float:
        """Apply a function to the results of one named timer."""
        if name in self._timings:
            return func(self._timings[name])
        raise KeyError(name)

def test_edge_case():
    timers = Timers()
    
    # Test with None
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "none_test")
    
    # Test with empty list
    timers._timings["empty_list_test"] = []
    assert timers.apply(lambda x: sum(x), "empty_list_test") == 0

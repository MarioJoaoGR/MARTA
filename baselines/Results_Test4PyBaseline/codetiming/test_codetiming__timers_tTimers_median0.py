
import pytest
from collections import defaultdict
import statistics
from typing import List, Dict, Callable, Any

class Timers:
    """Custom dictionary that stores information about timers."""
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize a new Timers instance.
        
        Args:
            *args (Any): Variable length argument list for superclass initialization.
            **kwargs (Any): Arbitrary keyword arguments for superclass initialization.
            
        This method initializes a private dictionary to keep track of all timings, using `collections.defaultdict(list)` to store timing results under keys as strings.
        """
        super().__init__(*args, **kwargs)
        self._timings: Dict[str, List[float]] = defaultdict(list)

    def apply(self, func: Callable[[List[float]], float], name: str) -> float:
        """Apply a function to the results of one named timer.
        
        Args:
            func (Callable[[List[float]], float]): A callable that takes a list of floats and returns a float.
            name (str): The name of the timer whose results will be passed to `func`.
            
        Returns:
            float: The result of applying `func` to the list of timing results associated with `name`.
        
        Raises:
            KeyError: If the specified `name` does not exist in the timers dictionary.
        
        Example:
            >>> timers = Timers()
            >>> timers._timings['example_timer'] = [1.0, 2.0, 3.0]
            >>> result = timers.apply(lambda x: sum(x), 'example_timer')
            >>> print(result)  # Output will be 6.0
        """
        if name in self._timings:
            return func(self._timings[name])
        raise KeyError(f"Timer '{name}' not found.")

    def median(self, name: str) -> float:
        """Calculate the median of the timing results for a specified timer.
        
        Args:
            name (str): The name of the timer whose results will be used to calculate the median.
            
        Returns:
            float: The median value of the timing results associated with `name`. If no timings are available, it returns 0.
        
        Example:
            >>> timers = Timers()
            >>> timers._timings['example_timer'] = [1.0, 2.0, 3.0]
            >>> median_time = timers.median('example_timer')
            >>> print(median_time)  # Output will be 2.0
        """
        return self.apply(lambda values: statistics.median(values or [0]), name=name)

# Test cases for Timers class
def test_timers_init():
    timers = Timers()
    assert isinstance(timers._timings, defaultdict)
    assert all(isinstance(v, list) for v in timers._timings.values())

def test_apply_existing_name():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    result = timers.apply(lambda x: sum(x), 'example_timer')
    assert result == 6.0

def test_apply_non_existing_name():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), 'nonexistent_timer')

def test_median_with_values():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    median_time = timers.median('example_timer')
    assert median_time == 2.0

def test_median_without_values():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median('nonexistent_timer')


import pytest
from collections import defaultdict
from typing import List, Dict, Any
import codetiming._timers as timers_module

class Timers(timers_module.Timers):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._timings: Dict[str, List[float]] = defaultdict(list)
    
    def min(self, name: str) -> float:
        values = self._timings.get(name, [0])
        return min(values)

def test_valid_input():
    timers = Timers()
    timers._timings['operation1'].append(1.0)
    timers._timings['operation1'].append(2.0)
    
    assert timers.min('operation1') == 1.0

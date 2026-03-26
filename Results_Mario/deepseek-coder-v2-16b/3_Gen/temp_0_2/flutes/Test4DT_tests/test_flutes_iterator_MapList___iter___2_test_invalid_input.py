
import pytest
from typing import Callable, Sequence, Iterator
import bisect

class MapList:
    def __init__(self, func: Callable[[int], int], lst: Sequence[int]):
        self.func = func
        self.list = lst
    
    def __iter__(self) -> Iterator[int]:
        return map(self.func, self.list)

def test_invalid_input():
    a = [1, 2, 3, 4, 5]
    with pytest.raises(TypeError):
        bisect.bisect_left(MapList(None, a), 10)

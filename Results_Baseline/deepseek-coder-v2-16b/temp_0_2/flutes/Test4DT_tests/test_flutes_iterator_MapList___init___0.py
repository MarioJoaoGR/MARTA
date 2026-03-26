
# Module: flutes.iterator
import pytest
from typing import Callable, Sequence, TypeVar
import bisect

T = TypeVar('T')  # Declare type variable T
R = TypeVar('R')  # Declare type variable R

class MapList(Sequence[T]):
    def __init__(self, func: Callable[[T], R], lst: Sequence[T]):
        self.func = func
        self.list = lst

    def __getitem__(self, idx):
        if isinstance(idx, int):
            return self.func(self.list[idx])
        return [self.func(x) for x in self.list[idx]]

    def __iter__(self):
        return map(self.func, self.list)

    def __len__(self):
        return len(self.list)

# Example list and function to transform elements
a = [1, 2, 3, 4, 5]
mapped_list = MapList(lambda x: x * x, a)

def test_maplist_getitem_int():
    assert mapped_list[0] == 1  # Output: 1 (1^2)

def test_maplist_getitem_slice():
    assert mapped_list[1:3] == [4, 9]  # Output: [4, 9] (2^2 and 3^2)

def test_maplist_iter():
    result = []
    for item in mapped_list:
        result.append(item)
    assert result == [1, 4, 9, 16, 25]

def test_maplist_bisect_left():
    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3  # Output: 3 (index of the first element whose square is >= 10)

# Run tests with pytest
if __name__ == "__main__":
    pytest.main()

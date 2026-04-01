
import unittest
from typing import Callable, Sequence, Iterator, TypeVar

T = TypeVar('T')
R = TypeVar('R')

class MapList:
    def __init__(self, func: Callable[[T], R], lst: Sequence[T]):
        self.func = func
        self.list = lst

    def __iter__(self) -> Iterator[R]:
        return map(self.func, self.list)

class TestMapList(unittest.TestCase):
    def test_valid_case(self):
        ml = MapList(lambda x: x * 2, [1, 2, 3])
        result = list(ml)
        self.assertEqual(result, [2, 4, 6])

if __name__ == "__main__":
    unittest.main()

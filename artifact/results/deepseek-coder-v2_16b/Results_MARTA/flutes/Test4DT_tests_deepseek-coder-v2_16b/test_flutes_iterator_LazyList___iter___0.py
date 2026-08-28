
import pytest
from typing import List, Iterable, TypeVar
import weakref

T = TypeVar('T')

class LazyList:
    'A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.'
    
    def __init__(self, iterable: Iterable[T]):
        self.iter = iter(iterable)
        self.exhausted = False
        self.list: List[T] = []

    class LazyListIterator:
        def __init__(self, lst: 'LazyList[T]'):
            self.list = weakref.ref(lst)
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            try:
                obj = self.list()[self.index]
            except IndexError:
                raise StopIteration
            self.index += 1
            return obj

    def __iter__(self):
        if self.exhausted:
            return iter(self.list)
        return self.LazyListIterator(self)

    def __getitem__(self, index: int) -> T:
        while len(self.list) <= index:
            try:
                item = next(self.iter)
                self.list.append(item)
            except StopIteration:
                raise IndexError("Index out of range")
        return self.list[index]

    def __len__(self):
        with pytest.raises(NotImplementedError):
            len(self)

def test_lazy_list_iteration():
    numbers = [1, 2, 3, 4]
    lazy_list = LazyList(numbers)
    result = []
    for item in lazy_list:
        result.append(item)
    assert result == [1, 2, 3, 4]


if __name__ == "__main__":
    pytest.main()
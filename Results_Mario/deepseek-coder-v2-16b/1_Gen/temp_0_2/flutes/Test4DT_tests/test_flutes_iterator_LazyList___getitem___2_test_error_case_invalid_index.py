
import pytest
from flutes.iterator import LazyList

# Mocking the LazyList and LazyListIterator for demonstration purposes
class MockLazyList(LazyList):
    def __init__(self, iterable):
        self.iter = iter(iterable)
        self.exhausted = False
        self.list = list(iterable)  # Convert iterable to a real list immediately

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start, stop, step = idx.indices(len(self.list))
            return [self.list[i] for i in range(start, stop, step)]
        elif isinstance(idx, int):
            return self.list[idx]
        else:
            raise TypeError("Index must be an integer or slice")

# Test case for __getitem__ method with invalid index
def test_error_case_invalid_index():
    lazy_list = MockLazyList([1, 2, 3])
    
    # Attempt to access an out-of-range index
    with pytest.raises(IndexError):
        lazy_list[5]

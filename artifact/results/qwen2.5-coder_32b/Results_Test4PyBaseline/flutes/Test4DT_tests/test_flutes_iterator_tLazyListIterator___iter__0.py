
# Module: flutes.iterator (or in the same file if not part of a separate module)
class LazyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

class LazyListIterator:
    def __init__(self, lazy_list):
        self.lazy_list = lazy_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lazy_list):
            result = self.lazy_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

def test_lazylistiterator_initialization():
    lazy_list = LazyList([1, 2, 3])
    iterator = LazyListIterator(lazy_list)
    assert iterator.index == 0

def test_lazylistiterator_iteration():
    lazy_list = LazyList([1, 2, 3])
    iterator = LazyListIterator(lazy_list)
    assert list(iterator) == [1, 2, 3]

def test_lazylistiterator_next():
    lazy_list = LazyList([1, 2, 3])
    iterator = LazyListIterator(lazy_list)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3

def test_lazylistiterator_exhaustion():
    lazy_list = LazyList([1, 2, 3])
    iterator = LazyListIterator(lazy_list)
    list(iterator)  # Exhaust the iterator
    try:
        next(iterator)
    except StopIteration:
        assert True
    else:
        assert False, "StopIteration not raised"


import weakref

# Define a simple LazyList class for demonstration
class LazyList:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)

# Define the LazyListIterator class as provided in the source code
class LazyListIterator:
    def __init__(self, lst: 'LazyList'):
        self.list = weakref.ref(lst)
        self.index = 0

    def __next__(self) -> 'T':
        try:
            obj = self.list()[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return obj
    
    def __iter__(self):
        return self

# Test file for LazyListIterator
def test_lazylistiterator_next_single_element():
    lazy_list = LazyList([42])
    iterator = LazyListIterator(lazy_list)
    assert next(iterator) == 42

def test_lazylistiterator_next_multiple_elements():
    lazy_list = LazyList([10, 20, 30])
    iterator = LazyListIterator(lazy_list)
    assert next(iterator) == 10
    assert next(iterator) == 20

def test_lazylistiterator_next_exhausted():
    lazy_list = LazyList([])
    iterator = LazyListIterator(lazy_list)
    try:
        next(iterator)
    except StopIteration as e:
        assert isinstance(e, StopIteration)

def test_lazylistiterator_next_stopiteration():
    lazy_list = LazyList([1])
    iterator = LazyListIterator(lazy_list)
    assert next(iterator) == 1
    try:
        next(iterator)
    except StopIteration as e:
        assert isinstance(e, StopIteration)

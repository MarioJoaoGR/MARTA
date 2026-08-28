
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
def test_lazylistiterator_next_first_element():
    lazy_list = LazyList([10, 20, 30, 40])
    iterator = LazyListIterator(lazy_list)
    assert next(iterator) == 10

def test_lazylistiterator_next_second_element():
    lazy_list = LazyList([10, 20, 30, 40])
    iterator = LazyListIterator(lazy_list)
    next(iterator)  # Skip first element
    assert next(iterator) == 20

def test_lazylistiterator_next_third_element():
    lazy_list = LazyList([10, 20, 30, 40])
    iterator = LazyListIterator(lazy_list)
    next(iterator)  # Skip first element
    next(iterator)  # Skip second element
    assert next(iterator) == 30

def test_lazylistiterator_next_fourth_element():
    lazy_list = LazyList([10, 20, 30, 40])
    iterator = LazyListIterator(lazy_list)
    next(iterator)  # Skip first element
    next(iterator)  # Skip second element
    next(iterator)  # Skip third element
    assert next(iterator) == 40

def test_lazylistiterator_next_stop_iteration():
    lazy_list = LazyList([10, 20, 30, 40])
    iterator = LazyListIterator(lazy_list)
    for _ in range(4):
        next(iterator)  # Iterate through all elements
    try:
        next(iterator)
    except StopIteration as e:
        assert isinstance(e, StopIteration)

def test_lazylistiterator_next_empty_list():
    lazy_list = LazyList([])
    iterator = LazyListIterator(lazy_list)
    try:
        next(iterator)
    except StopIteration as e:
        assert isinstance(e, StopIteration)

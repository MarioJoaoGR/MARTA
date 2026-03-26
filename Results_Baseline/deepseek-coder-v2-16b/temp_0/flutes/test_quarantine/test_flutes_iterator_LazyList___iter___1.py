
import pytest
from flutes.iterator import LazyList
import bisect  # Importing here since it's used in multiple tests

# Test initialization with an iterable
def test_lazy_list_initialization():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert isinstance(lazy_list, LazyList)

# Test iteration over the lazy list
def test_lazy_list_iteration():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    iterated_elements = []
    for element in lazy_list:
        iterated_elements.append(element)
    assert iterated_elements == [1, 2, 3, 4, 5]

# Test accessing elements by index
def test_lazy_list_index_access():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3

# Test converting the lazy list to a regular Python list
def test_lazy_list_to_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    regular_list = list(lazy_list)
    assert regular_list == [1, 2, 3, 4, 5]

# Test creating a MapList and transforming elements
def test_map_list():
    def square(x):
        return x * x

    transformed_list = LazyList([1, 2, 3, 4, 5])
    mapped_list = [square(element) for element in transformed_list]
    assert mapped_list == [1, 4, 9, 16, 25]

# Test using MapList with bisect_left to find the index of an element whose transformation meets a certain condition
def test_map_list_bisect_left():
    def square(x):
        return x * x

    transformed_list = LazyList([1, 2, 3, 4, 5])
    mapped_list = [square(element) for element in transformed_list]
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3

# Test the LazyListIterator initialization and iteration
def test_lazy_list_iterator():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    iterator = iter(lazy_list)
    assert isinstance(iterator, LazyListIterator)
    
    iterated_elements = []
    for element in iterator:
        iterated_elements.append(element)
    assert iterated_elements == [1, 2, 3, 4, 5]

# Test the behavior when the list is exhausted during iteration
def test_lazy_list_iterator_exhausted():
    my_list = []
    lazy_list = LazyList(my_list)
    iterator = iter(lazy_list)
    
    with pytest.raises(StopIteration):
        while True:
            next(iterator)

# Test the behavior when accessing elements beyond the end of the list
def test_lazy_list_index_out_of_range():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    
    with pytest.raises(IndexError):
        element = lazy_list[len(my_list)]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___iter___1
flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___1.py:59:32: E0602: Undefined variable 'LazyListIterator' (undefined-variable)


"""
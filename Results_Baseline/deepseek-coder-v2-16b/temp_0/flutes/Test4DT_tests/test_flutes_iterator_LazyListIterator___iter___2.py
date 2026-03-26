# Module: flutes.iterator
import pytest
from typing import List
import weakref

# Assuming LazyList and its elements are defined somewhere
class LazyList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item(self, index):
        return self.items[index]

class LazyListIterator:
    """
    A class for iterating over elements of a LazyList.

    Parameters:
        lst (LazyList[T]): The lazy list to iterate over. This should be an instance of a class that implements the LazyList protocol or subclass.

    Attributes:
        list (weakref.ref): A weak reference to the LazyList object being iterated over.
        index (int): The current index in the iteration, starting from 0.

    Returns:
        Iterator[T]: An iterator that yields elements of the LazyList one by one.

    Example:
        To use this class, first ensure you have a LazyList instance. Then create an instance of LazyListIterator with the desired LazyList:
        
        ```python
        lazy_list = LazyList()  # Assuming LazyList is defined somewhere
        iterator = LazyListIterator(lazy_list)
        
        for item in iterator:
            print(item)
        ```

    This will iterate over each element of the `LazyList` and print them. Note that the `LazyList` class should support iteration, meaning it has a method to retrieve elements by index or similar functionality.
    """
    def __init__(self, lst: 'LazyList'):
        self.list = weakref.ref(lst)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            obj = self.list().get_item(self.index)
        except IndexError:
            raise StopIteration
        self.index += 1
        return obj

# Fixture to create a LazyList and an iterator for testing
@pytest.fixture
def lazy_list():
    lst = LazyList()
    lst.add_item(10)
    lst.add_item(20)
    lst.add_item(30)
    return lst

# Test case to check the iteration over a pre-defined LazyList
def test_lazy_list_iterator(lazy_list):
    iterator = LazyListIterator(lazy_list)
    items = []
    for item in iterator:
        items.append(item)
    assert items == [10, 20, 30]

# Test case to check the iteration over a pre-defined LazyList with additional elements
def test_lazy_list_iterator_additional_elements(lazy_list):
    lazy_list.add_item(40)
    iterator = LazyListIterator(lazy_list)
    items = []
    for item in iterator:
        items.append(item)
    assert items == [10, 20, 30, 40]

# Test case to check the iteration over an empty LazyList
def test_lazy_list_iterator_empty():
    lst = LazyList()
    iterator = LazyListIterator(lst)
    with pytest.raises(StopIteration):
        next(iterator)

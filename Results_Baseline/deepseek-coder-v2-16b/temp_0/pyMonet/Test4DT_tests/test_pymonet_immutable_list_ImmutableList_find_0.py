# Module: pymonet.immutable_list
import pytest
from pymonet.immutable_list import ImmutableList

# Test cases for the find method of ImmutableList class

def test_find_element_in_non_empty_list():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    result = lst.find(lambda x: x > 0)
    assert result == 1

def test_find_element_not_in_non_empty_list():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    result = lst.find(lambda x: x == 0)
    assert result is None

def test_find_element_in_empty_list():
    empty_lst = ImmutableList()
    result = empty_lst.find(lambda x: x == 1)
    assert result is None

def test_find_specific_type_of_object_in_non_empty_list():
    class Person:
        def __init__(self, name: str):
            self.name = name

    lst = ImmutableList(head=Person("Alice"), tail=ImmutableList(head=Person("Bob"), tail=None))
    result = lst.find(lambda x: isinstance(x, Person) and x.name == "Alice")
    assert result.name == "Alice"

def test_find_element_using_function_with_multiple_conditions():
    class Book:
        def __init__(self, title: str, author: str):
            self.title = title
            self.author = author

    lst = ImmutableList(head=Book("1984", "Orwell"), tail=ImmutableList(head=Book("To Kill a Mockingbird", "Lee"), tail=None))
    result = lst.find(lambda x: isinstance(x, Book) and x.author == "Orwell")
    assert result.title == "1984"

if __name__ == "__main__":
    pytest.main()

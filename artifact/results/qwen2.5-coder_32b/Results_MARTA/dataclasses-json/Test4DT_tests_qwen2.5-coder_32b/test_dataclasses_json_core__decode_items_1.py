
import pytest
from dataclasses import dataclass
from typing import List
from dataclasses_json.core import _decode_items, is_dataclass

@dataclass
class Person:
    name: str
    age: int

def test_decode_items_with_dataclass():
    """Test decoding a list of dictionaries into dataclass instances."""
    people_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    decoded_people = list(_decode_items(Person, people_dicts, infer_missing=False))
    assert decoded_people == [Person(name='Alice', age=30), Person(name='Bob', age=25)]

@dataclass
class Employee:
    name: str
    department: str = "Unknown"

def test_decode_items_with_dataclass_infer_missing():
    """Test decoding a list of dictionaries into dataclass instances with infer_missing=True."""
    employees_dicts = [{'name': 'Charlie'}, {'name': 'David', 'department': 'HR'}]
    decoded_employees = list(_decode_items(Employee, employees_dicts, infer_missing=True))
    assert decoded_employees == [Employee(name='Charlie', department='Unknown'), Employee(name='David', department='HR')]

def test_decode_items_with_supported_generic():
    """Test decoding a list of tuples into instances of a supported generic type."""
    from typing import List
    numbers = [(1,), (2,), (3,)]
    decoded_numbers = list(_decode_items(List[int], numbers, infer_missing=False))
    assert decoded_numbers == [[1], [2], [3]]

def test_decode_items_with_unsupported_type():
    """Test decoding with a type that is neither a dataclass nor a supported generic."""
    simple_list = [1, 2, 3]
    decoded_simple_list = list(_decode_items(int, simple_list, infer_missing=False))
    assert decoded_simple_list == [1, 2, 3]

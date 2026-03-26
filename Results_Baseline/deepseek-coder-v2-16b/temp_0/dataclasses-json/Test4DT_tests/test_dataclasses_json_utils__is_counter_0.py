
import pytest
from collections import Counter
from typing import List, Union
from dataclasses_json.utils import _is_counter

def test_is_counter_subclass():
    my_list = List[int]
    assert not _is_counter(my_list), "Expected False as List[int] is not a subclass of Counter"

def test_is_counter_union():
    mixed_types = Union[int, str]
    assert not _is_counter(mixed_types), "Expected False as Union[int, str] is not a subclass of Counter"

def test_is_counter_custom_class():
    class MyCustomClass:
        pass

    assert not _is_counter(MyCustomClass), "Expected False as MyCustomClass does not inherit from Counter"

def test_is_counter_list():
    my_standard_list = [1, 2, 3]
    assert not _is_counter(my_standard_list), "Expected False as a standard list is not a subclass of Counter"

def test_is_counter_counter():
    my_counter = Counter([1, 2, 3])
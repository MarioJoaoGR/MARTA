
import pytest
from apimd.parser import _attr

class Example:
    nested = {'key': 'value'}

class AnotherExample:
    nested_dict = {'key1': {'key2': 'value'}}


def test_nonexistent_attribute():
    another_obj = None
    result = _attr(another_obj, 'non.existent.path')
    assert result is None

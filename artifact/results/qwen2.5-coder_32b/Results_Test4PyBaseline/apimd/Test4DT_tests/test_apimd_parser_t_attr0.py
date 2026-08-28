
import pytest
from apimd.parser import _attr

class Example:
    def __init__(self):
        self.level1 = Level1()

class Level1:
    def __init__(self):
        self.level2 = Level2()

class Level2:
    def __init__(self):
        self.value = 42

def test_attr_with_nested_objects():
    example = Example()
    assert _attr(example, 'level1.level2.value') == 42
    assert _attr(example, 'level1.level2') is not None
    assert isinstance(_attr(example, 'level1.level2'), Level2)

def test_attr_with_missing_attribute():
    example = Example()
    assert _attr(example, 'level1.missing') is None
    assert _attr(example, 'missing.level2.value') is None

def test_attr_with_dict():
    data = {'a': {'b': {'c': 10}}}
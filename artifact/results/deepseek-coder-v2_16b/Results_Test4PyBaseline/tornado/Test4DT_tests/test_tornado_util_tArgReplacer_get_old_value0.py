
import pytest
from typing import Callable, Sequence, Dict, Any
from unittest.mock import patch

# Import the ArgReplacer class from the tornado.util module
from tornado.util import ArgReplacer

def example_function(a, b=2):
    pass

@pytest.fixture
def arg_replacer():
    return ArgReplacer(example_function, 'b')

# Test initialization with a function and argument name
def test_init():
    func = example_function
    name = 'b'
    replacer = ArgReplacer(func, name)
    assert replacer.name == name
    assert isinstance(replacer.arg_pos, int)

# Test retrieving the old value of an argument when it exists
def test_get_old_value_exists(arg_replacer):
    args = ()
    kwargs = {'b': 10}
    old_value = arg_replacer.get_old_value(args, kwargs)
    assert old_value == 10

# Test retrieving the old value of an argument when it does not exist
def test_get_old_value_not_exists(arg_replacer):
    args = ()
    kwargs = {'a': 1}
    default_value = 'default'
    old_value = arg_replacer.get_old_value(args, kwargs, default_value)

import pytest
from unittest.mock import patch, MagicMock
from py_backwards.utils.helpers import get_source
from types import FunctionType
import re

def example_function():
    """Example docstring."""
    pass

def test_valid_input():
    with patch('py_backwards.utils.helpers.getsource', return_value='\n'.join([
        'def example_function():',
        '    """Example docstring."""',
        '    pass'
    ])):
        assert get_source(example_function) == 'def example_function():\n    """Example docstring."""\n    pass'

def test_none_input():
    with pytest.raises(TypeError):
        get_source(None)

def test_invalid_input():
    with pytest.raises(TypeError):
        get_source([])

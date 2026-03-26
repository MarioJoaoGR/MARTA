
import warnings
from unittest.mock import patch
import pytest

class MyClass:
    def __init__(self):
        self._cache = None
    
    def getter(self):
        warnings.warn('%s.cache is deprecated' % self.__class__.__name__, DeprecationWarning, 2)
        return self._cache

def test_none_input():
    my_instance = MyClass()
    with patch('warnings.warn') as mock_warn:
        result = my_instance.getter()
        assert result is None
        # Check if the deprecation warning was emitted
        mock_warn.assert_called_once_with('%s.cache is deprecated' % MyClass.__name__, DeprecationWarning, 2)

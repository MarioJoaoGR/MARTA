
import warnings
import pytest
from unittest.mock import patch

class MyClass:
    def __init__(self):
        self._cache = 'valid_value'
    
    def getter(self):
        warnings.warn('%s.cache is deprecated' % self.__class__.__name__, DeprecationWarning, 2)
        return self._cache

def test_getter():
    my_instance = MyClass()
    with pytest.deprecated_call():
        assert my_instance.getter() == 'valid_value'

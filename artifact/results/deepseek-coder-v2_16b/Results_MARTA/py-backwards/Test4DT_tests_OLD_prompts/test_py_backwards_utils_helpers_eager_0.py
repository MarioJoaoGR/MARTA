
import pytest
from py_backwards.utils.helpers import eager
from typing import Iterable, List, Callable, Any
from unittest.mock import patch

def test_eager_function():
    @eager
    def generate_numbers():
        for i in range(10):
            yield i
    
    result = generate_numbers()
    assert isinstance(result, list), "Expected a list but got something else"
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "Unexpected values in the list"

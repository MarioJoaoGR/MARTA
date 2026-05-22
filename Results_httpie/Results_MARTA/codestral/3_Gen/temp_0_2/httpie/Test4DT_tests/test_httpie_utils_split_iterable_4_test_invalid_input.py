
import pytest
from httpie.utils import split_iterable
from typing import Iterable, List, Tuple, Callable, TypeVar
from unittest.mock import patch

T = TypeVar('T')

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test passing an unsupported type for iterable
        split_iterable(None, lambda x: x % 2 == 0)  # None is not an Iterable
        
    with pytest.raises(TypeError):
        # Test passing a non-callable type for key function
        split_iterable([1, 2, 3], "not_a_callable")  # "not_a_callable" is not callable

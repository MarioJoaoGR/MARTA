
import pytest
from httpie.utils import split_iterable
from typing import Iterable, List, Tuple, Callable, TypeVar
from unittest.mock import patch

T = TypeVar('T')

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test with a non-callable argument as key function
        split_iterable([1, 2, 3], "not_a_callable")


import pytest
from docstring_parser.numpydoc import _pairwise
import itertools
import typing as T

def test_invalid_input():
    with pytest.raises(TypeError):
        list(_pairwise(42))  # Passing a non-iterable (int) should raise TypeError

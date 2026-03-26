
import pytest
from docstring_parser.numpydoc import _pairwise
import itertools
import types

def test_invalid_input():
    with pytest.raises(TypeError):
        result = _pairwise(42)  # Passing a non-iterable object to trigger TypeError

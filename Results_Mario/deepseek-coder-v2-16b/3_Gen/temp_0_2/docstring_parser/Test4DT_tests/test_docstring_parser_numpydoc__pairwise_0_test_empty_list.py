
import pytest
from docstring_parser.numpydoc import _pairwise
import itertools

def test_empty_list():
    iterable = []
    result = list(_pairwise(iterable))
    assert result == [], "Expected an empty list for an empty input"

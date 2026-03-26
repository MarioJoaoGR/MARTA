
import pytest
from docstring_parser.tests.test_numpydoc import parse, compose

def test_empty_input():
    source = ""
    expected = ""
    assert compose(parse(source)) == expected

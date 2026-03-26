
import pytest
from docstring_parser.tests.test_google import parse, test_short_description

def test_empty_input():
    source = ''
    expected = None  # Since the function expects an optional parameter and defaults to empty string, we should expect None for both short and long descriptions if no input is provided.
    
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta

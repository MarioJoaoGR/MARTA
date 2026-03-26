
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_missing_deprecation():
    source = 'Example source string without deprecation'
    expected_depr_version = None
    expected_depr_desc = None
    
    docstring = parse(source)
    
    assert docstring.deprecation is None

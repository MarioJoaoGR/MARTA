
import pytest
from tornado.options import _Option

# Test case for parsing a boolean value correctly
def test_parse_bool():
    opt = _Option(name='example', type=bool, default=None)
    
    # Test with valid true values
    assert opt._parse_bool('True') is True
    assert opt._parse_bool('true') is True
    assert opt._parse_bool('T') is True
    assert opt._parse_bool('t') is True
    assert opt._parse_bool('1') is True
    
    # Test with valid false values
    assert opt._parse_bool('False') is False
    assert opt._parse_bool('false') is False
    assert opt._parse_bool('F') is False
    assert opt._parse_bool('f') is False
    assert opt._parse_bool('0') is False
    
    # Test with invalid values
    assert opt._parse_bool('maybe') is True  # Default to True for unexpected inputs
    assert opt._parse_bool('no') is True      # Default to True for unexpected inputs

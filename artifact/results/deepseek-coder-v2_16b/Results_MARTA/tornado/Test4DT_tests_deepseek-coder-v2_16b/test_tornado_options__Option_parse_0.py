
import pytest
from tornado.options import _Option

# Test scenario: Creating an option with a default value and checking its type

# Test scenario: Creating an invalid option without specifying the type
def test_invalid_option():
    with pytest.raises(ValueError):
        opt = _Option(name='example_option', default=10, help='This is an example option')

# Test scenario: Parsing a valid string value for an option of type int
def test_parse_valid_int():
    opt = _Option(name='example_option', type=int, default=10, help='This is an example option')
    parsed_value = opt.parse('20')
    assert parsed_value == 20, f"Expected value to be 20 but got {parsed_value}"

# Test scenario: Parsing an invalid string value for an option of type int
def test_parse_invalid_int():
    opt = _Option(name='example_option', type=int, default=10, help='This is an example option')
    with pytest.raises(ValueError):
        opt.parse('not_an_integer')

# Test scenario: Parsing a valid string value for an option of type str
def test_parse_valid_str():
    opt = _Option(name='example_option', type=str, default='default_value', help='This is an example option')
    parsed_value = opt.parse('new_value')
    assert parsed_value == 'new_value', f"Expected value to be 'new_value' but got {parsed_value}"

# Test scenario: Parsing an invalid string value for an option of type str
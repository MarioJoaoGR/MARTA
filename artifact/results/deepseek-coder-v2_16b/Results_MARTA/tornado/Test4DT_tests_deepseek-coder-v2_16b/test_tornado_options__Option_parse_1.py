
import pytest
from tornado.options import _Option

# Test for default value when multiple is True and default is None
def test_default_value_when_multiple():
    opt = _Option(name='example_option', type=int, default=None, multiple=True)
    assert isinstance(opt.default, list), "Default should be a list"
    assert opt.default == [], "Default value for multiple options should be an empty list"

# Test for parsing a valid integer when multiple is True
def test_parse_valid_integer_multiple():
    opt = _Option(name='example_option', type=int, default=None, multiple=True)
    parsed_value = opt.parse("1,2,3")
    assert isinstance(parsed_value, list), "Parsed value should be a list"
    assert parsed_value == [1, 2, 3], "Parsed values should be [1, 2, 3]"

# Test for parsing an invalid type when multiple is True
def test_parse_invalid_type_multiple():
    opt = _Option(name='example_option', type=int, default=None, multiple=True)
    with pytest.raises(ValueError):
        opt.parse("1,2,three")

# Test for parsing a valid string when multiple is True
def test_parse_valid_string_multiple():
    opt = _Option(name='example_option', type=str, default=None, multiple=True)
    parsed_value = opt.parse("one,two,three")
    assert isinstance(parsed_value, list), "Parsed value should be a list"
    assert parsed_value == ["one", "two", "three"], "Parsed values should be ['one', 'two', 'three']"

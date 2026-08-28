
import pytest
from tornado.options import _Option

# Test case for checking if default value is None when multiple is True and default is not provided
def test_default_value_when_multiple():
    opt = _Option(name='example_option', type=int, default=None, multiple=True)
    assert isinstance(opt.default, list), "Default should be a list when multiple is True"
    assert len(opt.default) == 0, "Default list should be empty when not provided explicitly"

# Test case for checking if type must not be None
def test_type_must_not_be_none():
    with pytest.raises(ValueError):
        _Option(name='example_option', type=None)

# Test case for checking if default value is preserved when provided explicitly
def test_default_value_provided():
    opt = _Option(name='example_option', type=int, default=10)
    assert opt.default == 10, "Default value should be preserved when provided"


import pytest
from tornado.options import _Option

# Test valid input scenario
def test_valid_input():
    opt = _Option(name='example_option', type=int, default=10)
    assert opt.name == 'example_option'
    assert opt.type == int
    assert opt.default == 10
    assert opt._value == _Option.UNSET

# Test edge case scenario with None and empty list for multiple options
def test_edge_case():
    opt = _Option(name='multiple_example', type=str, multiple=True)
    assert opt.name == 'multiple_example'
    assert opt.type == str
    assert opt.multiple is True
    assert opt.default == []
    assert opt._value == _Option.UNSET

# Test invalid input scenario raising ValueError
def test_invalid_input():
    with pytest.raises(ValueError):
        opt = _Option(name='error_option', type=None)

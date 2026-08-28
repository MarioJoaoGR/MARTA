
# Module: tornado.options
# test_tornado_options.py
from tornado.options import _Option
import pytest

# Test creating an instance of _Option with required parameters
def test_init_required_params():
    opt = _Option(name="example_option", type=int)
    assert opt.name == "example_option"
    assert opt.type == int
    assert opt.default is None
    assert opt._value == _Option.UNSET

# Test creating an instance of _Option with all parameters (including optional ones)
def test_init_all_params():
    opt = _Option(name="example_option", default=10, type=int, help="This is an example option.", metavar="EXAMPLE")
    assert opt.name == "example_option"
    assert opt.default == 10
    assert opt.type == int
    assert opt.help == "This is an example option."
    assert opt.metavar == "EXAMPLE"
    assert not opt.multiple
    assert opt._value == _Option.UNSET

# Test creating an instance of _Option with multiple values enabled
def test_init_multiple():
    opt = _Option(name="example_option", type=int, multiple=True)
    assert opt.name == "example_option"
    assert opt.type == int
    assert opt.default == []
    assert opt.multiple
    assert opt._value == _Option.UNSET

# Test setting a valid value for an option without multiple values
def test_set_valid_value():
    opt = _Option(name="example_option", type=int)
    opt.set(15)
    assert opt._value == 15

# Test setting a list of valid values for an option with multiple values enabled
def test_set_multiple_valid_values():
    opt = _Option(name="example_option", type=int, multiple=True)
    opt.set([15, 20])

import pytest
from tornado.options import _Option

# Test initialization with required parameters only
def test_init_required():
    opt = _Option(name='example_option', type=int)
    assert opt.name == 'example_option'
    assert opt.type == int
    assert opt.default is None
    assert opt._value == _Option.UNSET

# Test initialization with default value, type, and help text
def test_init_with_default():
    opt = _Option(name='example_option', default=10, type=int, help="This is an example option.")
    assert opt.name == 'example_option'
    assert opt.type == int
    assert opt.default == 10
    assert opt.help == "This is an example option."
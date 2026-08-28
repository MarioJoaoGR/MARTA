
import pytest
from tornado.options import _Option
import re
import datetime

@pytest.fixture
def basic_option():
    return _Option(name="example_option", type=int)

@pytest.fixture
def full_option():
    return _Option(name="example_option", default=10, type=int, help="This is an example option.", metavar="EXAMPLE")

@pytest.fixture
def multiple_option():
    return _Option(name="example_option", type=str, multiple=True)

@pytest.fixture
def callback_option():
    def callback_function(value):
        print("Callback called with value:", value)
    return _Option(name="example_option", type=str, callback=callback_function)

def test_basic_option_creation(basic_option):
    assert basic_option.name == "example_option"
    assert basic_option.type == int
    assert basic_option.default is None
    with pytest.raises(ValueError):
        _Option(name="example_option", type=None)

def test_full_option_creation(full_option):
    assert full_option.name == "example_option"
    assert full_option.type == int
    assert full_option.default == 10
    assert full_option.help == "This is an example option."
    assert full_option.metavar == "EXAMPLE"
    assert not full_option.multiple

def test_multiple_option_creation(multiple_option):
    assert multiple_option.name == "example_option"
    assert multiple_option.type == str
    assert isinstance(multiple_option.default, list) and not multiple_option.default

def test_callback_option_creation(callback_option):
    assert callback_option.name == "example_option"
    assert callback_option.type == str
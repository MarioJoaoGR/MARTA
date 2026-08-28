
# Module: tornado.options
# test_tornado_options.py
from tornado.options import OptionParser
import pytest

@pytest.fixture
def parser():
    return OptionParser()

def test_define(parser):
    # Define an option with default type str
    parser.define("test_option", help="Test help")
    assert hasattr(parser, "test_option"), "Option 'test_option' should be defined"
    assert parser.test_option is None, f"Default value for 'test_option' should be None, but got {parser.test_option}"  # Default value should be None for string type

    # Define an option with int type
    parser.define("int_option", type=int, help="Int option test")
    assert hasattr(parser, "int_option"), "Option 'int_option' should be defined"

# Module: tornado.options
# test_tornado_options.py
from tornado.options import OptionParser, define
import pytest

@pytest.fixture(scope="module")
def parser():
    # Create an instance of OptionParser for each test module
    return OptionParser()

def test_define_option(parser):
    """Test defining a new option."""
    parser.define("test_port", type=int, help="TCP port to listen on")
    assert hasattr(parser, "test_port"), "Option 'test_port' should be defined."

# New test case for __getitem__ method coverage
def test_getitem_existing_attribute(parser):
    """Test accessing an existing attribute via __getitem__."""
    parser.define("test_attr", type=str, help="A test attribute")
    assert parser["test_attr"] == getattr(parser, "test_attr"), "Accessing existing attribute should return its value."

# New test case for non-existing attribute handling
def test_getitem_non_existing_attribute(parser):
    """Test accessing a non-existing attribute via __getitem__."""
    with pytest.raises(AttributeError):
        parser["nonexistent_attr"]

# New test case to ensure defaults are handled correctly
def test_getitem_with_defaults(parser):
    """Test handling of attributes from defaults when accessing via __getitem__."""
    define("test_default", default="default_value", help="A default test attribute")

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

# Module: tornado.options
# test_tornado_options.py
from tornado.options import OptionParser, define, parse_command_line
import pytest
import sys

@pytest.fixture
def parser():
    return OptionParser()

def test_define_option(parser):
    """Test defining an option with a default value and type."""
    parser.define("port", int, "TCP port to listen on")
    assert hasattr(parser, "port"), "Expected 'port' attribute to be defined"

import pytest
from tornado.options import OptionParser, define

# Test initialization of OptionParser
def test_optionparser_initialization():
    parser = OptionParser()
    assert hasattr(parser, '_options') and isinstance(parser._options, dict)
    assert hasattr(parser, '_parse_callbacks') and isinstance(parser._parse_callbacks, list)

# Test define method with default values
def test_define_method():
    parser = OptionParser()
    parser.define("port", type=int, help="TCP port to listen on")
    assert "port" in parser._options

# New test case to cover the __iter__ method of OptionParser
def test_optionparser_iter():
    parser = OptionParser()
    define("port", default=8080, type=int, help="TCP port to listen on")
    define("host", default="127.0.0.1", type=str, help="Host IP address")
    
    # Ensure the __iter__ method returns an iterator over option names
    options_names = [opt for opt in parser]
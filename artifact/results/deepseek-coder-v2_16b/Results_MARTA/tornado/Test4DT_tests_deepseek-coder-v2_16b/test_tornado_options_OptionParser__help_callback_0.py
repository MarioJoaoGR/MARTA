
import pytest
from tornado.options import OptionParser


def test_invalid_inputs():
    parser = OptionParser()
    parser.define('port', int, 'The port to listen on')
    parser.define('debug', bool, 'Enable debug mode')
    
    # Parse invalid inputs
    args = ['--invalid_option']
    with pytest.raises(AttributeError):
        parser.parse(args)

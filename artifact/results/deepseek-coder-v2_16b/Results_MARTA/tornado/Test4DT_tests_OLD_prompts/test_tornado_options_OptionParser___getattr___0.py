
import pytest
from tornado.options import OptionParser, _Option

def test_OptionParser___getattr___basic():
    parser = OptionParser()
    
    # Define a mock option with default value and type
    parser._options['mock'] = _Option('mock', default=None, type=str)
    
    assert parser.mock == None

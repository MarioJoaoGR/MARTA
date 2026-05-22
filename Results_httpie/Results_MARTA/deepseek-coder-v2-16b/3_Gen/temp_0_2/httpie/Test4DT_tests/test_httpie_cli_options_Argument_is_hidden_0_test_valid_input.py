
import pytest
from unittest.mock import patch
from httpie.cli.options import Qualifiers

class Argument:
    def __init__(self):
        self.configuration = {}
    
    def is_hidden(self):
        return self.configuration.get('help') is Qualifiers.SUPPRESS

def test_valid_input():
    arg = Argument()
    arg.configuration = {'help': Qualifiers.SUPPRESS}
    
    with patch('httpie.cli.options.Qualifiers', new=Qualifiers):
        assert arg.is_hidden() is True

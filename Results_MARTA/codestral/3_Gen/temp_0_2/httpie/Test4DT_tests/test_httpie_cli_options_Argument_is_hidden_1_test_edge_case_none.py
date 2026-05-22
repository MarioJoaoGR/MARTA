
import pytest
from unittest.mock import patch
from httpie.cli.options import Qualifiers

class Argument:
    def __init__(self):
        self.configuration = {}
    
    def is_hidden(self):
        return self.configuration.get('help') is Qualifiers.SUPPRESS

def test_edge_case_none():
    arg = Argument()
    with patch.object(arg, 'configuration', {'help': None}):
        assert not arg.is_hidden(), "Expected help text to be shown when configuration is None"

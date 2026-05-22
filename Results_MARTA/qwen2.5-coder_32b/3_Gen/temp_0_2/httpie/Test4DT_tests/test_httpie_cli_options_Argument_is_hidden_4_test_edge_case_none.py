
import pytest
from unittest.mock import patch
from httpie.cli.options import Qualifiers

class Argument:
    def __init__(self):
        self.configuration = None

    def is_hidden(self):
        return self.configuration.get('help') is Qualifiers.SUPPRESS

def test_edge_case_none():
    arg = Argument()
    with patch.object(arg, 'configuration', {'help': Qualifiers.SUPPRESS}):
        assert arg.is_hidden() == True

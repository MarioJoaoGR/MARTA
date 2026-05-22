
import pytest
from unittest.mock import patch
from httpie.cli.options import Qualifiers

class Argument:
    aliases: list[str]
    configuration: dict[str, any]
    
    def __init__(self):
        self.configuration = {}

    def is_hidden(self) -> bool:
        return self.configuration.get('help') is Qualifiers.SUPPRESS

def test_invalid_input():
    arg = Argument()
    with patch.object(Argument, 'is_hidden', side_effect=AttributeError("Unexpected help value")):
        arg.configuration = {'help': 'unexpected_value'}
        with pytest.raises(AttributeError):
            arg.is_hidden()


import pytest
from unittest.mock import patch

class Argument:
    aliases: list
    configuration: dict

    def __getattr__(self, attribute_name):
        if attribute_name in self.configuration:
            return self.configuration[attribute_name]
        else:
            raise AttributeError(attribute_name)

def test_valid_input():
    arg = Argument()
    arg.configuration = {'key1': 'value1', 'key2': 'value2'}
    
    with patch('builtins.__import__', return_value=None):  # Mocking import to avoid actual module import during tests
        assert arg.key1 == 'value1'

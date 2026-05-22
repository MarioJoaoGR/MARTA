
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import KeyValueArgType, Escaped

@pytest.fixture(autouse=True)
def setup_key_value_arg_type():
    kvat = KeyValueArgType('=', ',', ';')
    return kvat

def test_valid_input(setup_key_value_arg_type):
    with patch('httpie.cli.argtypes.KeyValueArgType.tokenize') as mock_tokenize:
        # Mock the tokenize method to return a predefined list of tokens
        mock_tokenize.return_value = ['foo=bar', 'baz=qux']
        
        kvat = setup_key_value_arg_type
        result = kvat.tokenize('foo=bar,baz=qux')
        
        assert result == ['foo=bar', 'baz=qux']

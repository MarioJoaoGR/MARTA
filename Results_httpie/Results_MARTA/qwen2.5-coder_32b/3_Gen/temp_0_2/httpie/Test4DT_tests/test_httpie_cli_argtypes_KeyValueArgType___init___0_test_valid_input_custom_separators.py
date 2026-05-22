
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import KeyValueArgType

@pytest.fixture(autouse=True)
def setup_key_value_arg_type():
    with patch('httpie.cli.argtypes.KeyValueArgType', autospec=True):
        yield KeyValueArgType(',', ';')

def test_valid_input_custom_separators():
    key_value_arg_type = KeyValueArgType(',', ';')
    assert key_value_arg_type.separators == (',', ';')

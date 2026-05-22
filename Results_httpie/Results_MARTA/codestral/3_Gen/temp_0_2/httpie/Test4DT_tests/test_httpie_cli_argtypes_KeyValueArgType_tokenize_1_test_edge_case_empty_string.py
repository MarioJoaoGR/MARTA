
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import KeyValueArgType, Escaped

@pytest.fixture(autouse=True)
def setup_key_value_arg_type():
    return KeyValueArgType('=')

def test_edge_case_empty_string(setup_key_value_arg_type):
    kvat = setup_key_value_arg_type
    with patch.object(kvat, 'tokenize', side_effect=lambda s: [''] if not s else [s]):
        result = kvat.tokenize('')
        assert result == ['']


import pytest
from httpie.cli.argtypes import KeyValueArgType, Escaped

@pytest.fixture
def key_value_parser():
    return KeyValueArgType()

def test_edge_case(key_value_parser):
    with pytest.raises(AssertionError):
        tokens = key_value_parser.tokenize('foo=bar')
        assert tokens == ['foo', '=', 'bar']

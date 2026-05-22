
import pytest
from httpie.cli.argtypes import KeyValueArgType, Escaped

@pytest.fixture
def kvat():
    return KeyValueArgType('=')

def test_tokenize_edge_case(kvat):
    result = kvat.tokenize(r'foo\=bar\\baz')
    assert result == ['foo', Escaped('='), 'bar\\\\baz']


import pytest
from httpie.cli.argtypes import KeyValueArgType, Escaped

def test_tokenize():
    key_value_parser = KeyValueArgType('\\=')
    tokens = key_value_parser.tokenize(r'foo\=bar')
    assert tokens == ['foo', Escaped('='), 'bar']

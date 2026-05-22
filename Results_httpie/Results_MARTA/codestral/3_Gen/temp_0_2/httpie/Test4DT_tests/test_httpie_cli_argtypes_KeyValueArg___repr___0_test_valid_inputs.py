
import pytest
from httpie.cli.argtypes import KeyValueArg

def test_valid_inputs():
    # Test valid key-value pairs with different separators
    kv1 = KeyValueArg("key", "value", ":", "key:value")
    assert kv1.key == "key"
    assert kv1.value == "value"
    assert kv1.sep == ":"
    assert kv1.orig == "key:value"

    kv2 = KeyValueArg("key", None, ":=", "key:=value")
    assert kv2.key == "key"
    assert kv2.value is None  # Corrected assertion to check the value directly

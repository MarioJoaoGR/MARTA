
import pytest
from httpie.cli.argtypes import KeyValueArg

@pytest.mark.parametrize("key, value, sep, orig", [
    ("key1", "value1", ":", "key1:value1"),
    ("key2", None, ":", "key2:"),
    ("key3", "value3", "=", "key3=value3"),
    ("key4", None, "=", "key4=")
])
def test_valid_inputs(key, value, sep, orig):
    kv1 = KeyValueArg(key, value, sep, orig)
    kv2 = KeyValueArg(key, value, sep, orig)
    assert kv1 == kv2

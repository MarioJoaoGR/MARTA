
import pytest
from ansible.module_utils.common.text.converters import to_text

def test_valid_string():
    obj = "Hello, World!"
    result = to_text(obj)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == "Hello, World!", f"Expected 'Hello, World!' but got '{result}'"

def test_valid_bytes():
    obj = b'Hello, World!'
    result = to_text(obj)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == "Hello, World!", f"Expected 'Hello, World!' but got '{result}'"


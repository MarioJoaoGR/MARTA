
import pytest
from typing import Optional

class KeyValueArg:
    def __init__(self, key: str = "", value: Optional[str] = None, sep: str = "", orig: str = ""):
        self.key = key
        self.value = value
        self.sep = sep
        self.orig = orig

def process_header_arg(arg: KeyValueArg) -> Optional[str]:
    return arg.value or None

# Test cases for process_header_arg function

# Example 1: Providing a valid KeyValueArg object with no value specified (only the key and separator are provided)
def test_process_header_arg_no_value():
    kv_arg = KeyValueArg(key="Content-Type", sep=":")
    assert process_header_arg(kv_arg) is None, "Expected None since value is not specified"

# Example 2: Providing a valid KeyValueArg object with an empty value string
def test_process_header_arg_empty_value():
    kv_arg = KeyValueArg(key="Content-Type", value="", sep=":", orig="Content-Type:")
    assert process_header_arg(kv_arg) is None, "Expected None since value is an empty string"

# Example 3: Providing a valid KeyValueArg object with a None value
def test_process_header_arg_none_value():
    kv_arg = KeyValueArg(key="Content-Type", value=None, sep=":", orig="Content-Type:")
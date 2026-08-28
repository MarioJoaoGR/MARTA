
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

# Example 1: Providing a valid KeyValueArg object with a value attribute
def test_process_header_arg_valid():
    kv_arg = KeyValueArg(key="Content-Type", value="application/json", sep=":", orig="Content-Type:application/json")
    assert process_header_arg(kv_arg) == "application/json"

# Example 2: Providing a valid KeyValueArg object without a value attribute
def test_process_header_arg_no_value():
    kv_arg_no_value = KeyValueArg(key="Authorization", value=None, sep=":", orig="Authorization:")
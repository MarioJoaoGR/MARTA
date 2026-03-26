
import pytest
from typing import Dict, Any
from isort._vendored.tomli._parser import loads

def test_valid_input_simple_toml():
    toml_string = "key=42"
    parsed_data = loads(toml_string)
    assert parsed_data == {'key': 42}

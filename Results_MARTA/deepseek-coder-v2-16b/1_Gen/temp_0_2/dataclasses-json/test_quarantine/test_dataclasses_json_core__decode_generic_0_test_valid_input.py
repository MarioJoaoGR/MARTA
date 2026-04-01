
import pytest
from dataclasses import dataclass
from typing import Optional, Union
from json import loads
from dataclasses_json.core import _decode_generic
from dataclasses_json.core import is_dataclass

# Mock class X for testing
@dataclass
class X:
    a: int
    b: str
    c: Optional[float] = None

def test_valid_input():
    # Valid JSON string
    json_str = '{"a": 1, "b": "test", "c": 3.14}'
    
    # Deserialize the JSON string to dataclass X
    decoded_x = _decode_generic(X, loads(json_str), True)
    
    # Check if the deserialization is correct
    assert isinstance(decoded_x, X)
    assert decoded_x.a == 1
    assert decoded_x.b == "test"
    assert decoded_x.c == 3.14

if __name__ == "__main__":
    pytest.main()

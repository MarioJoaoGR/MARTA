
import pytest
from dataclasses_json.core import _encode_overrides  # Assuming this function is in a module named 'dataclasses_json.core'
from dataclasses import dataclass, fields
from typing import Dict, Any, Callable

# Define OverrideInfo for completeness, though it might be part of the imported module
@dataclass
class OverrideInfo:
    letter_case: Callable[[str], str] = None
    encoder: Callable[[Any], Any] = None
    exclude: Callable[[Any], bool] = None

# Mock data for testing
kvs = {'name': 'John Doe', 'age': 30}
overrides = {
    'name': OverrideInfo(letter_case=lambda x: x.upper(), encoder=None),
    'age': OverrideInfo(letter_case=None, encoder=str)
}

def test_encode_overrides():
    encoded_dict = _encode_overrides(kvs, overrides)
    assert encoded_dict == {'NAME': 'John Doe', 'age': '30'}

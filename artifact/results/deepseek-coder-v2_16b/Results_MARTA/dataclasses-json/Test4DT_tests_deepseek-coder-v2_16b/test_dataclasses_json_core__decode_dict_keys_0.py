
import pytest
from dataclasses_json.core import _decode_dict_keys
from dataclasses import dataclass
from typing import List, Optional, Any

# Define a simple dataclass for demonstration
@dataclass
class DataClassExample:
    value: int



def test_decode_dict_keys_without_type():
    decoded_keys = _decode_dict_keys(None, ['foo', 'bar'], infer_missing=True)
    assert list(decoded_keys) == ['foo', 'bar']

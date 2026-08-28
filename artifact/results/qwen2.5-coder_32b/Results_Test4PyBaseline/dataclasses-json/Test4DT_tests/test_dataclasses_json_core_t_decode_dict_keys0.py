
import pytest
from dataclasses_json.core import _decode_dict_keys
from typing import Any, Optional
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

def test_decode_dict_keys_int():
    result = list(_decode_dict_keys(int, {'1': 'one', '2': 'two'}, infer_missing=False))
    assert result == [1, 2]

def test_decode_dict_keys_none():
    result = list(_decode_dict_keys(None, {'a': 1, 'b': 2}, infer_missing=False))

import pytest
from typing import Set
from datetime import datetime, date
from ansible.module_utils.common.text.converters import _json_encode_fallback

def test_serialize_set():
    my_set = set([1, 2, 3])
    serialized_set = _json_encode_fallback(my_set)
    assert isinstance(serialized_set, list), f"Expected a list but got {type(serialized_set)}"
    assert sorted(serialized_set) == [1, 2, 3], f"Expected [1, 2, 3] but got {serialized_set}"

def test_serialize_datetime():
    dt = datetime.now()
    serialized_dt = _json_encode_fallback(dt)
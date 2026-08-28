
import pytest
from typing import Set
from datetime import datetime, timedelta
from ansible.module_utils.common.text.converters import _json_encode_fallback

def test_serialize_set():
    my_set = set([1, 2, 3])
    serialized_set = _json_encode_fallback(my_set)
    assert isinstance(serialized_set, list), f"Expected a list but got {type(serialized_set)}"
    assert sorted(serialized_set) == [1, 2, 3], f"Expected [1, 2, 3] but got {serialized_set}"

def test_serialize_datetime():
    dt = datetime.now()
    serialized_dt = _json_encode_fallback(dt)
    assert isinstance(serialized_dt, str), f"Expected a string representation of the datetime object, but got {type(serialized_dt)}"
    # Further validation could be added to check if the output is in ISO format

def test_serialize_timedelta():
    td = timedelta(days=1, seconds=2, microseconds=3, milliseconds=4, minutes=5, hours=6, weeks=7)
    with pytest.raises(TypeError):
        _json_encode_fallback(td)

def test_unsupported_type():
    class UnsupportedType:
        pass
    
    unsupported = UnsupportedType()
    with pytest.raises(TypeError):
        _json_encode_fallback(unsupported)

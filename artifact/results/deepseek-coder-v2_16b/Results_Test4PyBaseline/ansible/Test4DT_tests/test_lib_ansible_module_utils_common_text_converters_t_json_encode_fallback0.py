
# Module: ansible.module_utils.common.text.converters
import pytest
from typing import Set
from datetime import datetime

# Import the function from its module
try:
    from ansible.module_utils.common.text.converters import _json_encode_fallback
except ImportError:
    # If the import fails, assume the function is not available in this environment
    pytestmark = pytest.mark.skip(reason="Function not available in this environment")

def test_serialize_set():
    my_set = set([1, 2, 3])
    serialized_set = _json_encode_fallback(my_set)
    assert serialized_set == [1, 2, 3], f"Expected [1, 2, 3] but got {serialized_set}"

def test_serialize_datetime():
    dt = datetime.now()
    serialized_dt = _json_encode_fallback(dt)
    assert isinstance(serialized_dt, str), f"Expected a string representation of the datetime object, but got {type(serialized_dt)}"
    # Further validation could be added to check if the output is in ISO format

def test_unsupported_type():
    class UnsupportedType:
        pass
    
    unsupported = UnsupportedType()
    with pytest.raises(TypeError) as excinfo:
        _json_encode_fallback(unsupported)
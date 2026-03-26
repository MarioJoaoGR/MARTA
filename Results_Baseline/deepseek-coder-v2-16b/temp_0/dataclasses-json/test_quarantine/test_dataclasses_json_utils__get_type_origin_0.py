
# Module: dataclasses_json.utils
import pytest
from typing import List, Union, Optional
import sys

# Assuming the function implementation and constants are as provided in the docstring
if sys.version_info.minor == 6:
    _NO_TYPE_ORIGIN = object()
else:
    _NO_TYPE_ORIGIN = None

def test_get_type_origin_with_list():
    from dataclasses_json import get_type_origin as _get_type_origin  # Assuming this is the correct module and function name
    my_list = List[int]
    assert _get_type_origin(my_list) == list

def test_get_type_origin_with_union():
    from dataclasses_json import get_type_origin as _get_type_origin  # Assuming this is the correct module and function name
    mixed_types = Union[int, str]
    assert _get_type_origin(mixed_types) in (int, str)

def test_get_type_origin_with_optional():
    from dataclasses_json import get_type_origin as _get_type_origin  # Assuming this is the correct module and function name
    maybe_none = Optional[int]
    assert _get_type_origin(maybe_none) == int or _get_type_origin(maybe_none) is None

def test_get_type_origin_with_unknown_origin():
    from dataclasses_json import get_type_origin as _get_type_origin  # Assuming this is the correct module and function name
    my_list = List[int]
    mixed_types = Union[int, str]
    maybe_none = Optional[int]
    
    assert _get_type_origin(my_list) == list
    assert _get_type_origin(mixed_types) in (int, str)
    assert _get_type_origin(maybe_none) is None or _get_type_origin(maybe_none) == int

def test_get_type_origin_with_invalid_type():
    from dataclasses_json import get_type_origin as _get_type_origin  # Assuming this is the correct module and function name
    with pytest.raises(AttributeError):
        invalid_type = 123  # Assuming this is an invalid type for the function to handle
        _get_type_origin(invalid_type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:14:4: E0611: No name 'get_type_origin' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:19:4: E0611: No name 'get_type_origin' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:24:4: E0611: No name 'get_type_origin' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:29:4: E0611: No name 'get_type_origin' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:39:4: E0611: No name 'get_type_origin' in module 'dataclasses_json' (no-name-in-module)

"""

import pytest
from collections import Collection
from dataclasses_json.utils import _get_type_origin, _issubclass_safe

def test_invalid_input():
    # Test with an invalid type that is not a class or generic type
    with pytest.raises(TypeError):
        assert _is_collection(int)  # int is not a class, it's a built-in type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_collection_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_invalid_input.py:3:0: E0611: No name 'Collection' in module 'collections' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_invalid_input.py:9:15: E0602: Undefined variable '_is_collection' (undefined-variable)


"""
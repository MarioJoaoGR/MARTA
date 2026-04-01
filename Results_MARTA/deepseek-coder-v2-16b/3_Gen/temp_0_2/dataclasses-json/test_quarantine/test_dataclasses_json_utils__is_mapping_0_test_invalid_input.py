
import pytest
from collections import Mapping
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe

def test_invalid_input():
    class MyDict(dict): pass
    assert not _is_mapping(MyDict)
    
    class MyList(list): pass
    assert not _is_mapping(MyList)
    
    assert _is_mapping(dict)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_invalid_input.py:3:0: E0611: No name 'Mapping' in module 'collections' (no-name-in-module)


"""

from collections import Mapping
import pytest
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe

def test_edge_case_none():
    class MyDict(dict): pass
    assert _is_mapping(MyDict) == True
    
    class MyList(list): pass
    assert _is_mapping(MyList) == False
    
    assert _is_mapping(dict) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_0_test_edge_case_none
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_edge_case_none.py:2:0: E0611: No name 'Mapping' in module 'collections' (no-name-in-module)


"""
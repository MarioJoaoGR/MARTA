
import pytest
from dataclasses_json.utils import Collection, _is_nonstr_collection

def test_valid_case_list():
    from typing import List
    assert _is_nonstr_collection(List[int]) == True
    
    class MyDeque(deque): pass
    assert _is_nonstr_collection(MyDeque) == False
    
    assert _is_nonstr_collection(dict) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_nonstr_collection_0_test_valid_case_list
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_nonstr_collection_0_test_valid_case_list.py:9:18: E0602: Undefined variable 'deque' (undefined-variable)


"""
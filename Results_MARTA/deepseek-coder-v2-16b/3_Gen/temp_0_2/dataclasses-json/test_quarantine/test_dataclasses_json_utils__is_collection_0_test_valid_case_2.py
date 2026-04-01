
import pytest
from collections import Collection, deque
from dataclasses_json.utils import _is_collection as is_collection

class MyDeque(deque): pass
class MyList(list): pass

def test_valid_case_2():
    assert is_collection(MyDeque) == True
    assert is_collection(MyList) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_collection_0_test_valid_case_2
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_valid_case_2.py:3:0: E0611: No name 'Collection' in module 'collections' (no-name-in-module)


"""
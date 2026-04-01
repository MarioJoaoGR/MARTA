
import pytest
from collections import deque, Collection
from dataclasses_json.utils import _is_collection, _get_type_origin

def test_valid_case_1():
    class MyDeque(deque): pass
    assert _is_collection(MyDeque) == True

    class MyList(list): pass
    assert _is_collection(MyList) == False

    from typing import List
    my_typed_list = List[int]
    assert _is_collection(my_typed_list) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_collection_0_test_valid_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_valid_case_1.py:3:0: E0611: No name 'Collection' in module 'collections' (no-name-in-module)


"""
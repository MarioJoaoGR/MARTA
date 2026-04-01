
import pytest
from collections import Collection
from dataclasses_json.utils import _is_collection, _get_type_origin, _issubclass_safe

def test_valid_case():
    from collections import deque
    
    my_deque = deque([1, 2, 3])
    assert _is_collection(my_deque) == True
    
    class MyList:
        def __iter__(self):
            yield 1
    
    my_custom_list = MyList()
    assert _is_collection(my_custom_list) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_collection_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_valid_case.py:3:0: E0611: No name 'Collection' in module 'collections' (no-name-in-module)

"""
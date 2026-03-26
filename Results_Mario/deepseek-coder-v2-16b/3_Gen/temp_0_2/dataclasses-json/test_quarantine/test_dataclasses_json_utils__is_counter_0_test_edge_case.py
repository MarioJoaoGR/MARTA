
import pytest
from collections import Counter
from your_module_name import _get_type_origin, _issubclass_safe  # Replace 'your_module_name' with the actual module name where `_is_counter` is defined.

def test_edge_case():
    class MyCounter(Counter): pass
    
    assert _is_counter(MyCounter) == True, "Expected MyCounter to be a subclass of Counter"
    
    class NotACounter: pass
    
    assert _is_counter(NotACounter) == False, "Expected NotACounter not to be a subclass of Counter"
    
    from typing import List
    my_list = List[int]
    assert _is_counter(my_list) == False, "Expected List[int] not to be a subclass of Counter"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_counter_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_0_test_edge_case.py:4:0: E0401: Unable to import 'your_module_name' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_0_test_edge_case.py:9:11: E0602: Undefined variable '_is_counter' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_0_test_edge_case.py:13:11: E0602: Undefined variable '_is_counter' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_0_test_edge_case.py:17:11: E0602: Undefined variable '_is_counter' (undefined-variable)


"""
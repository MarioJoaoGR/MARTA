
import pytest

class A: pass
class B(A): pass
class C: pass
class D(str): pass

def test_valid_case_1():
    assert _is_new_type_subclass_safe(B, A) == True
    assert _is_new_type_subclass_safe(C, int) == False
    assert _is_new_type_subclass_safe(D, str) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_valid_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_valid_case_1.py:10:11: E0602: Undefined variable '_is_new_type_subclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_valid_case_1.py:11:11: E0602: Undefined variable '_is_new_type_subclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_subclass_safe_2_test_valid_case_1.py:12:11: E0602: Undefined variable '_is_new_type_subclass_safe' (undefined-variable)


"""
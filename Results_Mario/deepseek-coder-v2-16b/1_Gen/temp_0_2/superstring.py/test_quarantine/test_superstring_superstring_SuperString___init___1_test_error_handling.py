
from superstring.superstring import SuperString
import pytest

def test_error_handling():
    with pytest.raises(TypeError):
        SuperString("content", previous=0, i=None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperString___init___1_test_error_handling
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___1_test_error_handling.py:7:8: E1123: Unexpected keyword argument 'previous' in constructor call (unexpected-keyword-arg)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___1_test_error_handling.py:7:8: E1123: Unexpected keyword argument 'i' in constructor call (unexpected-keyword-arg)


"""
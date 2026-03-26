
import pytest
from SortAttempt import SortAttempt

def test_invalid_inputs():
    with pytest.raises(TypeError):
        attempt = SortAttempt('not a bool', 'also not a bool', 'neither is this')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main_SortAttempt___init___1_test_invalid_inputs
isort/Test4DT_tests/test_isort_main_SortAttempt___init___1_test_invalid_inputs.py:3:0: E0401: Unable to import 'SortAttempt' (import-error)


"""
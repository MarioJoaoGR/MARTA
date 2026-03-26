
import pytest
from sortattempt import SortAttempt  # Assuming the class is defined in a file named sortattempt.py

def test_invalid_inputs():
    with pytest.raises(TypeError):
        attempt = SortAttempt(incorrectly_sorted='not a bool', skipped=[], supported_encoding=123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main_SortAttempt___init___2_test_invalid_inputs
isort/Test4DT_tests/test_isort_main_SortAttempt___init___2_test_invalid_inputs.py:3:0: E0401: Unable to import 'sortattempt' (import-error)


"""
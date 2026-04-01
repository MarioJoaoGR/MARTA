
import pytest
from SortAttempt import SortAttempt

def test_valid_inputs():
    attempt = SortAttempt(incorrectly_sorted=True, skipped=False, supported_encoding=True)
    assert attempt.incorrectly_sorted is True
    assert attempt.skipped is False
    assert attempt.supported_encoding is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main_SortAttempt___init___0_test_valid_inputs
isort/Test4DT_tests/test_isort_main_SortAttempt___init___0_test_valid_inputs.py:3:0: E0401: Unable to import 'SortAttempt' (import-error)


"""
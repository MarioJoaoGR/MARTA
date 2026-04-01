
import pytest

def test_empty_string():
    value = ''
    result = _as_list(value)
    assert result == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__as_list_2_test_empty_string
isort/Test4DT_tests/test_isort_settings__as_list_2_test_empty_string.py:6:13: E0602: Undefined variable '_as_list' (undefined-variable)


"""
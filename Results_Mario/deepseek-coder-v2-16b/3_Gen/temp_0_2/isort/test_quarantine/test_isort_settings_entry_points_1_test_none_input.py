
import pytest
from importlib.metadata import entry_points

def test_none_input():
    with pytest.raises(TypeError):
        entry_points(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_entry_points_1_test_none_input
isort/Test4DT_tests/test_isort_settings_entry_points_1_test_none_input.py:7:8: E1121: Too many positional arguments for function call (too-many-function-args)


"""
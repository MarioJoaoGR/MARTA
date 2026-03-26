
from importlib.metadata import entry_points as ep  # noqa: PLC0415
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        entry_points("my_group")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_entry_points_0_test_invalid_input
isort/Test4DT_tests/test_isort_settings_entry_points_0_test_invalid_input.py:7:8: E0602: Undefined variable 'entry_points' (undefined-variable)


"""
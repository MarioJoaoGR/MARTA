
import pytest
from importlib.metadata import entry_points

def entry_points(group: str) -> "EntryPoints":
    """Call entry_point after lazy loading it.

    TODO: The reason for lazy loading here are unknown.
    """
    from importlib.metadata import entry_points as ep  # noqa: PLC0415

    return ep(group=group)

def test_none_input():
    with pytest.raises(TypeError):
        entry_points(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_entry_points_1_test_none_input
isort/Test4DT_tests/test_isort_settings_entry_points_1_test_none_input.py:5:0: E0102: function already defined line 3 (function-redefined)


"""
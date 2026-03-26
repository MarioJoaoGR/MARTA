
# Module: isort.wrap_modes
# test_formatter_from_string.py
import pytest
from isort.wrap_modes import formatter_from_string, grid, table

def test_valid_grid():
    """Test that the function returns the correct callable for a valid 'GRID' input."""
    result = formatter_from_string('GRID')
    assert result == grid

def test_invalid_input():
    """Test that the function defaults to 'grid' when an invalid input is provided."""
    result = formatter_from_string('INVALID')
    assert result == grid

def test_valid_table():
    """Test that the function returns the correct callable for a valid 'TABLE' input."""
    result = formatter_from_string('TABLE')
    assert result == table

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes_formatter_from_string_0
isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0.py:5:0: E0611: No name 'table' in module 'isort.wrap_modes' (no-name-in-module)


"""
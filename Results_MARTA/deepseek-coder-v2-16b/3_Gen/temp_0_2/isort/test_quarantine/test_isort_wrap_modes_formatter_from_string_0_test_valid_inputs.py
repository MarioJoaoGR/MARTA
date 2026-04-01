
import pytest
from isort.wrap_modes import _wrap_modes, grid

def formatter_from_string(name: str) -> Callable[..., str]:
    return _wrap_modes.get(name.upper(), grid)

# Test cases for valid inputs
@pytest.mark.parametrize("input_mode, expected", [
    ("GRID", grid),
    ("TABLE", _wrap_modes["table"]),
    ("INVALID", grid)
])
def test_valid_inputs(input_mode, expected):
    assert formatter_from_string(input_mode) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes_formatter_from_string_0_test_valid_inputs
isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_valid_inputs.py:5:40: E0602: Undefined variable 'Callable' (undefined-variable)


"""
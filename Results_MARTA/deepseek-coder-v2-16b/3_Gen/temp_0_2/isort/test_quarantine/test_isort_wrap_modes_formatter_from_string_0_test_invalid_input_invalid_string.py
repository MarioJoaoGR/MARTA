
import pytest
from isort.wrap_modes import _wrap_modes, grid

def formatter_from_string(name: str) -> Callable[..., str]:
    return _wrap_modes.get(name.upper(), grid)

def test_invalid_input_invalid_string():
    with pytest.raises(KeyError):
        formatter_from_string('INVALID')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes_formatter_from_string_0_test_invalid_input_invalid_string
isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_invalid_input_invalid_string.py:5:40: E0602: Undefined variable 'Callable' (undefined-variable)


"""
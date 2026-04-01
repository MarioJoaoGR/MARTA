
# Importing grid and table from the correct module
from isort.wrap_modes import grid, table

def formatter_from_string(name: str) -> Callable[..., str]:
    return _wrap_modes.get(name.upper(), grid)

# Test case for valid input
def test_valid_input():
    assert callable(formatter_from_string('GRID'))
    assert formatter_from_string('GRID') == grid
    
    assert callable(formatter_from_string('TABLE'))
    assert formatter_from_string('TABLE') == table
    
    assert callable(formatter_from_string('INVALID'))
    assert formatter_from_string('INVALID') == grid

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes_formatter_from_string_0_test_valid_input
isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_valid_input.py:3:0: E0611: No name 'table' in module 'isort.wrap_modes' (no-name-in-module)
isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_valid_input.py:5:40: E0602: Undefined variable 'Callable' (undefined-variable)
isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_valid_input.py:6:11: E0602: Undefined variable '_wrap_modes' (undefined-variable)


"""
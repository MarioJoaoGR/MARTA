
import pytest
from isort.wrap_modes import _wrap_mode, _wrap_modes

@pytest.fixture(autouse=True)
def reset_wrap_modes():
    # Reset the _wrap_modes dictionary before each test to ensure no interference between tests
    _wrap_modes.clear()

def test_valid_input():
    @_wrap_mode
    def my_wrap_mode() -> str:
        return "wrapped"
    
    assert "_WRAP_MODES" in globals(), "The _wrap_modes dictionary should be defined globally."
    assert len(_wrap_modes) == 1, "There should be one registered wrap mode."
    assert "MY_WRAP_MODE" in _wrap_modes, "The registered wrap mode should have its name in uppercase."
    
    # Check the function's signature and annotations are consistent with _wrap_mode_interface
    my_func = _wrap_modes["MY_WRAP_MODE"]
    assert my_func.__signature__ == inspect.signature(_wrap_mode_interface)  # type: ignore
    assert my_func.__annotations__ == _wrap_mode_interface.__annotations__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes__wrap_mode_0_test_valid_input
isort/Test4DT_tests/test_isort_wrap_modes__wrap_mode_0_test_valid_input.py:21:36: E0602: Undefined variable 'inspect' (undefined-variable)
isort/Test4DT_tests/test_isort_wrap_modes__wrap_mode_0_test_valid_input.py:21:54: E0602: Undefined variable '_wrap_mode_interface' (undefined-variable)
isort/Test4DT_tests/test_isort_wrap_modes__wrap_mode_0_test_valid_input.py:22:38: E0602: Undefined variable '_wrap_mode_interface' (undefined-variable)


"""

import pytest
from isort.wrap_modes import _wrap_mode, _wrap_modes, _wrap_mode_interface
from inspect import signature
from typing import Callable

@pytest.fixture(autouse=True)
def reset_wrap_modes():
    # Reset the _wrap_modes dictionary before each test to ensure no interference between tests
    _wrap_modes.clear()

def test_valid_input():
    @_wrap_mode
    def example_wrap():
        pass
    
    assert "EXAMPLE_WRAP" in _wrap_modes
    assert callable(example_wrap)
    assert signature(example_wrap) == signature(_wrap_mode_interface)
    assert example_wrap.__annotations__ == _wrap_mode_interface.__annotations__

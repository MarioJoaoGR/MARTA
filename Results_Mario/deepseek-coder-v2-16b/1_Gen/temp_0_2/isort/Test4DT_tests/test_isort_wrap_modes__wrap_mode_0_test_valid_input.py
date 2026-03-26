
import pytest
from isort.wrap_modes import _wrap_mode, _wrap_modes, _wrap_mode_interface
from inspect import signature

def test_valid_input():
    @_wrap_mode
    def my_wrap_mode() -> str:
        return "wrapped"
    
    # Check if the function is registered correctly in _wrap_modes
    assert 'MY_WRAP_MODE' in _wrap_modes
    wrapped_function = _wrap_modes['MY_WRAP_MODE']
    
    # Check if the signature and annotations are correct
    assert wrapped_function.__signature__ == signature(_wrap_mode_interface)  # type: ignore
    assert wrapped_function.__annotations__ == _wrap_mode_interface.__annotations__

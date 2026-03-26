
from sty import Register
import pytest
from typing import Type, Callable, Any
from unittest.mock import MagicMock

def test_invalid_input():
    register = Register()
    
    # Mock a non-existent render type
    mock_rendertype = MagicMock()
    with pytest.raises(KeyError):
        register.set_rgb_call(mock_rendertype)

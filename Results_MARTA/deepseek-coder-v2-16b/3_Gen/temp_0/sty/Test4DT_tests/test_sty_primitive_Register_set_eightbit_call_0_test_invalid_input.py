
import pytest
from unittest.mock import MagicMock
from sty.primitive import RenderType, Register

def test_invalid_input():
    reg = Register()
    
    # Mocking an invalid render type that is not in the renderfuncs dictionary
    with pytest.raises(KeyError):
        reg.set_eightbit_call(MagicMock())  # Using MagicMock as a placeholder for an invalid RenderType

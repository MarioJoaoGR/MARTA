
import pytest
from sty import Register, RenderType

def test_set_none_as_rendertype():
    custom_register = Register()
    
    # Test setting None as a rendertype
    with pytest.raises(KeyError):
        custom_register.set_eightbit_call(None)

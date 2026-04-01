
import pytest
from sty.primitive import Register, RenderType  # Assuming 'sty.primitive' is correctly imported

def test_set_rgb_call_invalid_input():
    reg = Register()
    
    with pytest.raises(KeyError):
        reg.set_rgb_call("InvalidType")

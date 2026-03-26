
import pytest
from sty import register, Style, Sgr

@pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
def test_invalid_inputs(invalid_input):
    ef = register.EfRegister()
    
    with pytest.raises(TypeError):
        getattr(ef, invalid_input)

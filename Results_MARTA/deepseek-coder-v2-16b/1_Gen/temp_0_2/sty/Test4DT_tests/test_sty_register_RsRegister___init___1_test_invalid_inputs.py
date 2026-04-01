
import pytest
from sty import RsRegister, Style, Sgr, renderfunc

@pytest.fixture
def rs_register():
    return RsRegister()

def test_invalid_inputs(rs_register):
    with pytest.raises(AttributeError):
        assert rs_register.nonexistentattribute  # This should raise an AttributeError due to the invalid attribute access

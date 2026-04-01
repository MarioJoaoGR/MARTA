
import pytest
from sty import RsRegister, Style, Sgr, renderfunc

@pytest.fixture
def rs_register():
    return RsRegister()

def test_RsRegister_init(rs_register):
    assert isinstance(rs_register.all, Style)
    assert isinstance(rs_register.fg, Style)
    assert isinstance(rs_register.bg, Style)
    assert isinstance(rs_register.ef, Style)
    assert isinstance(rs_register.bold_dim, Style)
    assert isinstance(rs_register.dim_bold, Style)
    assert isinstance(rs_register.i, Style)
    assert isinstance(rs_register.italic, Style)
    assert isinstance(rs_register.u, Style)
    assert isinstance(rs_register.underl, Style)
    assert isinstance(rs_register.blink, Style)
    assert isinstance(rs_register.inverse, Style)
    assert isinstance(rs_register.hidden, Style)
    assert isinstance(rs_register.strike, Style)

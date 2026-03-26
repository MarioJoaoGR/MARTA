
import pytest
from sty import EfRegister, Style, Sgr, renderfunc

@pytest.fixture
def ef_register():
    return EfRegister()

def test_ef_register_init(ef_register):
    assert isinstance(ef_register.bold, Style)
    assert isinstance(ef_register.dim, Style)
    assert isinstance(ef_register.italic, Style)
    assert isinstance(ef_register.u, Style)
    assert isinstance(ef_register.underl, Style)
    assert isinstance(ef_register.blink, Style)
    assert isinstance(ef_register.inverse, Style)
    assert isinstance(ef_register.hidden, Style)
    assert isinstance(ef_register.strike, Style)
    assert isinstance(ef_register.rs, Style)

def test_renderfuncs_init(ef_register):
    assert Sgr in ef_register.renderfuncs
    assert ef_register.renderfuncs[Sgr] == renderfunc.sgr

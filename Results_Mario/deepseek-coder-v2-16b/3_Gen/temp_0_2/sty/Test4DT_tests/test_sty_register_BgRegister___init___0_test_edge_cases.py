
import pytest
from sty import register, Style

@pytest.fixture(scope="module")
def bg_register():
    return register.BgRegister()

def test_edge_cases(bg_register):
    assert isinstance(bg_register.black, Style)
    assert isinstance(bg_register.red, Style)
    assert isinstance(bg_register.green, Style)
    assert isinstance(bg_register.yellow, Style)
    assert isinstance(bg_register.blue, Style)
    assert isinstance(bg_register.magenta, Style)
    assert isinstance(bg_register.cyan, Style)
    assert isinstance(bg_register.li_grey, Style)
    assert isinstance(bg_register.rs, Style)
    assert isinstance(bg_register.da_grey, Style)
    assert isinstance(bg_register.li_red, Style)
    assert isinstance(bg_register.li_green, Style)
    assert isinstance(bg_register.li_yellow, Style)
    assert isinstance(bg_register.li_blue, Style)
    assert isinstance(bg_register.li_magenta, Style)
    assert isinstance(bg_register.li_cyan, Style)
    assert isinstance(bg_register.white, Style)
    assert isinstance(bg_register.da_black, Style)
    assert isinstance(bg_register.da_red, Style)
    assert isinstance(bg_register.da_green, Style)
    assert isinstance(bg_register.da_yellow, Style)
    assert isinstance(bg_register.da_blue, Style)
    assert isinstance(bg_register.da_magenta, Style)
    assert isinstance(bg_register.da_cyan, Style)
    assert isinstance(bg_register.grey, Style)

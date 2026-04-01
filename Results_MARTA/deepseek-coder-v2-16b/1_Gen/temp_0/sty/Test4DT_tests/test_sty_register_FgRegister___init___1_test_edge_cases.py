
from sty import FgRegister, Style, Sgr, EightbitFg, RgbFg, renderfunc
import pytest

@pytest.fixture
def fg():
    return FgRegister()

def test_edge_cases(fg):
    assert isinstance(fg.black, Style)
    assert isinstance(fg.red, Style)
    assert isinstance(fg.green, Style)
    assert isinstance(fg.yellow, Style)
    assert isinstance(fg.blue, Style)
    assert isinstance(fg.magenta, Style)
    assert isinstance(fg.cyan, Style)
    assert isinstance(fg.li_grey, Style)
    assert isinstance(fg.rs, Style)
    assert isinstance(fg.da_grey, Style)
    assert isinstance(fg.li_red, Style)
    assert isinstance(fg.li_green, Style)
    assert isinstance(fg.li_yellow, Style)
    assert isinstance(fg.li_blue, Style)
    assert isinstance(fg.li_magenta, Style)
    assert isinstance(fg.li_cyan, Style)
    assert isinstance(fg.white, Style)
    assert isinstance(fg.da_black, Style)
    assert isinstance(fg.da_red, Style)
    assert isinstance(fg.da_green, Style)
    assert isinstance(fg.da_yellow, Style)
    assert isinstance(fg.da_blue, Style)
    assert isinstance(fg.da_magenta, Style)
    assert isinstance(fg.da_cyan, Style)
    assert isinstance(fg.grey, Style)

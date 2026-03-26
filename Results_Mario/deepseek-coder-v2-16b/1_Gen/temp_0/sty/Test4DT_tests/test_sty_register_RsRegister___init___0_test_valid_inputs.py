
import pytest
from sty import Style, RsRegister

def test_valid_inputs():
    rs = RsRegister()
    
    assert isinstance(rs.all, Style)
    assert isinstance(rs.fg, Style)
    assert isinstance(rs.bg, Style)
    assert isinstance(rs.ef, Style)
    assert isinstance(rs.bold_dim, Style)
    assert isinstance(rs.dim_bold, Style)
    assert isinstance(rs.i, Style)
    assert isinstance(rs.italic, Style)
    assert isinstance(rs.u, Style)
    assert isinstance(rs.underl, Style)
    assert isinstance(rs.blink, Style)
    assert isinstance(rs.inverse, Style)
    assert isinstance(rs.hidden, Style)
    assert isinstance(rs.strike, Style)

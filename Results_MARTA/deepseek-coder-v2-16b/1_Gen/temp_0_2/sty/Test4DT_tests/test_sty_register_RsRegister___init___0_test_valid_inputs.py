
import pytest
from sty import register  # Assuming the correct import path is used based on your module structure

def test_valid_inputs():
    rs = register.RsRegister()
    
    assert isinstance(rs, register.RsRegister), "Expected RsRegister instance"
    assert isinstance(rs.all, register.Style), "Expected all to be a Style instance"
    assert isinstance(rs.fg, register.Style), "Expected fg to be a Style instance"
    assert isinstance(rs.bg, register.Style), "Expected bg to be a Style instance"
    assert isinstance(rs.ef, register.Style), "Expected ef to be a Style instance"
    assert isinstance(rs.bold_dim, register.Style), "Expected bold_dim to be a Style instance"
    assert isinstance(rs.dim_bold, register.Style), "Expected dim_bold to be a Style instance"
    assert isinstance(rs.i, register.Style), "Expected i to be a Style instance"
    assert isinstance(rs.italic, register.Style), "Expected italic to be a Style instance"
    assert isinstance(rs.u, register.Style), "Expected u to be a Style instance"
    assert isinstance(rs.underl, register.Style), "Expected underl to be a Style instance"
    assert isinstance(rs.blink, register.Style), "Expected blink to be a Style instance"
    assert isinstance(rs.inverse, register.Style), "Expected inverse to be a Style instance"
    assert isinstance(rs.hidden, register.Style), "Expected hidden to be a Style instance"
    assert isinstance(rs.strike, register.Style), "Expected strike to be a Style instance"

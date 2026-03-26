
import pytest
from sty import EfRegister, Style, Sgr
from sty.renderfunc import sgr as renderfunc_sgr

def test_invalid_inputs():
    ef = EfRegister()
    
    # Check if the instance has the correct attributes and types
    assert hasattr(ef, 'b')
    assert isinstance(ef.b, Style)
    assert hasattr(ef, 'bold')
    assert isinstance(ef.bold, Style)
    assert hasattr(ef, 'dim')
    assert isinstance(ef.dim, Style)
    assert hasattr(ef, 'i')
    assert isinstance(ef.i, Style)
    assert hasattr(ef, 'italic')
    assert isinstance(ef.italic, Style)
    assert hasattr(ef, 'u')
    assert isinstance(ef.u, Style)
    assert hasattr(ef, 'underl')
    assert isinstance(ef.underl, Style)
    assert hasattr(ef, 'blink')
    assert isinstance(ef.blink, Style)
    assert hasattr(ef, 'inverse')
    assert isinstance(ef.inverse, Style)
    assert hasattr(ef, 'hidden')
    assert isinstance(ef.hidden, Style)
    assert hasattr(ef, 'strike')
    assert isinstance(ef.strike, Style)
    assert hasattr(ef, 'rs')
    assert isinstance(ef.rs, Style)
    
    # Check if the renderfuncs attribute is correctly set
    assert Sgr in ef.renderfuncs
    assert ef.renderfuncs[Sgr] == renderfunc_sgr

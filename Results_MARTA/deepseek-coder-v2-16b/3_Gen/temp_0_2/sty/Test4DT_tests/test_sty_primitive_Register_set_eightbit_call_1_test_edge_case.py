
import pytest
from sty.primitive import Register, Renderfuncs

def test_edge_case():
    reg = Register()
    with pytest.raises(KeyError):
        reg.set_eightbit_call(None)

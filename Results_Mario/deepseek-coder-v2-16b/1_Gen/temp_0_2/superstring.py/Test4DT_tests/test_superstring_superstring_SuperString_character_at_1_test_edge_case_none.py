
import pytest
from superstring.superstring import SuperString

def test_edge_case_none():
    superstring = SuperString(None)
    with pytest.raises(TypeError):
        superstring.split()

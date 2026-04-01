
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

def test_edge_case_none():
    with pytest.raises(TypeError):
        base_string = SuperStringBase(None)

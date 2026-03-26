
import pytest
from superstring.superstring import SuperString, SuperStringUpper

def test_edge_case_none():
    with pytest.raises(TypeError):
        superstring_upper = SuperStringUpper(SuperString('Hello, World!'))
        superstring_upper.character_at(None)

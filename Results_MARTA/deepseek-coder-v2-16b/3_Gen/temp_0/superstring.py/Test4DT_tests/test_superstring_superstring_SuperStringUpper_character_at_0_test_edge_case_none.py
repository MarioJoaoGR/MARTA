
import pytest
from superstring.superstring import SuperStringBase, SuperStringUpper

def test_edge_case_none():
    with pytest.raises(TypeError):
        super_string = SuperStringUpper(SuperStringBase('Hello, World!'))
        char = super_string.character_at(None)

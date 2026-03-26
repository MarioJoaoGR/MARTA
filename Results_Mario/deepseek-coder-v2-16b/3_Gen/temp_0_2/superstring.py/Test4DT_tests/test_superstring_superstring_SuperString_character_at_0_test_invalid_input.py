
import pytest
from superstring.superstring import SuperString

def test_invalid_input():
    s = SuperString('Hello, World!')
    with pytest.raises(TypeError):
        s.character_at("invalid")

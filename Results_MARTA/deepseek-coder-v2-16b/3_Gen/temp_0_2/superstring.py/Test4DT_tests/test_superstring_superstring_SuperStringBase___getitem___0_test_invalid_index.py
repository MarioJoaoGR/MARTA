
import pytest
from superstring.superstring import SuperStringBase

def test_invalid_index():
    with pytest.raises(TypeError):
        s = SuperStringBase('Hello, World!')

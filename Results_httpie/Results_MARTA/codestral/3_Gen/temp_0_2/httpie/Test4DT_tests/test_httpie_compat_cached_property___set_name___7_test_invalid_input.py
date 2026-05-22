
import pytest
from httpie.compat import cached_property

def test_invalid_input():
    with pytest.raises(TypeError):
        cached_property()

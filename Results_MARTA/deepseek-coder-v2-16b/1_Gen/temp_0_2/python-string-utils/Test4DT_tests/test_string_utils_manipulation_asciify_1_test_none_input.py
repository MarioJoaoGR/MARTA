
import pytest
from string_utils.manipulation import asciify

def test_none_input():
    with pytest.raises(TypeError):
        asciify(None)

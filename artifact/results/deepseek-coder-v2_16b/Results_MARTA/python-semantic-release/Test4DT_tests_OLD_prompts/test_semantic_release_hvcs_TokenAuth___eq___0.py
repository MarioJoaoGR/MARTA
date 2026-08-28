
import pytest
from semantic_release.hvcs import TokenAuth

def test_invalid_inputs():
    with pytest.raises(TypeError):
        TokenAuth()  # This should raise a TypeError because the constructor requires an argument

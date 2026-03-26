
import pytest
from flutes.fs import remove_prefix

def test_invalid_input_none():
    with pytest.raises(TypeError):
        remove_prefix("test", None)  # Test invalid input with None type for prefix

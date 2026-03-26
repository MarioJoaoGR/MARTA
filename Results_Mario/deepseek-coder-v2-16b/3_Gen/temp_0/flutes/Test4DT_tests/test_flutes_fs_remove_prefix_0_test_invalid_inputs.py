
import pytest
from flutes.fs import remove_prefix

def test_invalid_inputs():
    # Test with invalid inputs that should raise a TypeError
    with pytest.raises(TypeError):
        remove_prefix(123, "https://")  # int instead of str
    
    with pytest.raises(TypeError):
        remove_prefix("https://github.com/huzecong/flutes", 123)  # int instead of str


import pytest
from flutes.fs import remove_suffix

def test_invalid_inputs():
    # Test with invalid inputs
    with pytest.raises(TypeError):
        remove_suffix(123, "suffix")  # s is not a string
    
    with pytest.raises(TypeError):
        remove_suffix("string", 456)  # suffix is not a string

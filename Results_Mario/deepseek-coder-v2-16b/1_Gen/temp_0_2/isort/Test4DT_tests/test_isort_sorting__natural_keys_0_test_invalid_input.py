
import pytest
from isort.sorting import _natural_keys

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test case where input is not a string
        _natural_keys(123)  # This should raise TypeError because the input is an integer

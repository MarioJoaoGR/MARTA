
import pytest
from pymonet.either import Left

# Test invalid input where initialization is incorrect
def test_invalid_input():
    with pytest.raises(TypeError):
        Left()  # This should raise a TypeError because it lacks the required argument 'value'

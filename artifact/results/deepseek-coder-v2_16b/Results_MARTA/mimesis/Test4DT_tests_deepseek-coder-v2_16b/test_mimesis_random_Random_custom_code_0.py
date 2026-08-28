
import pytest
from mimesis.random import Random

# Test default parameters

# Test custom mask with only characters

# Test custom mask and different placeholders

# Test invalid input with same placeholder for digits and chars
def test_invalid_input_same_placeholder():
    rand_gen = Random()
    with pytest.raises(ValueError):
        rand_gen.custom_code('@##', char='!', digit='!')
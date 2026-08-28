
import pytest
from pymonet.semigroups import Max

# Test for valid inputs

# Test for edge cases

# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        Max().combine()
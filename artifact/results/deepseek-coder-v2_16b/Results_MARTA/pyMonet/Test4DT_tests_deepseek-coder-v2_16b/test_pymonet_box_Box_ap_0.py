
import pytest
from pymonet.box import Box

# Test valid input where Box contains a value and an applicative function

# Test edge case where Box contains a value and an applicative function that is not callable
def test_invalid_applicative():
    box = Box(42)
    applicative_box = Box("not a callable")
    with pytest.raises(TypeError, match=".*is not callable"):
        result = box.ap(applicative_box)
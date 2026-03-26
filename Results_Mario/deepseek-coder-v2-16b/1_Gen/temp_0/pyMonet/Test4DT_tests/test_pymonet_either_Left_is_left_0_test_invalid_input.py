
import pytest
from pymonet.either import Left

def test_invalid_input():
    non_left_instance = None
    with pytest.raises(AttributeError):
        # Attempting to use an invalid instance should raise a TypeError
        assert non_left_instance.is_left()


import pytest
from pytutils.excs import ok

def test_invalid_input():
    with pytest.raises(TypeError):
        with ok() as cm:
            raise TypeError("Test exception")  # This should raise a TypeError because it's not an exception type

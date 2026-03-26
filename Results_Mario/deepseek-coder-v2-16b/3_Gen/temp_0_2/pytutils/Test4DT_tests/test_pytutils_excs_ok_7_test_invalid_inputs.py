
import pytest
from pytutils.excs import ok

def test_invalid_inputs():
    with pytest.raises(TypeError):
        with ok():
            raise TypeError("This is a TypeError")

    with pytest.raises(ValueError):
        with ok(ZeroDivisionError):
            raise ValueError("This is a ValueError")

    with pytest.raises(ZeroDivisionError):
        with ok(ValueError):
            raise ZeroDivisionError("This is a ZeroDivisionError")

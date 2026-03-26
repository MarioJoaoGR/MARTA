
import pytest
from pytutils.excs import ok

def test_no_exceptions():
    with ok():
        # No exception should be raised within this block
        pass

def test_none_type():
    with pytest.raises(TypeError):
        with ok() as cm:
            raise TypeError("Test type error")

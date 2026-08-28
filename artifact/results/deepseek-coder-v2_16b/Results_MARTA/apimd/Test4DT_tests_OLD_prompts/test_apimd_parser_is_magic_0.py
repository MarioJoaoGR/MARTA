
import pytest
from apimd.parser import is_magic



def test_invalid_inputs():
    with pytest.raises(AttributeError):
        is_magic(12345)  # Invalid input should raise AttributeError
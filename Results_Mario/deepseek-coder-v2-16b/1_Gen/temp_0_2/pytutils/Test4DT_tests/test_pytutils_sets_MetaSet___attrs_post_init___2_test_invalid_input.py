
import pytest
from pytutils.sets import MetaSet

def test_invalid_input():
    meta_set = MetaSet()
    
    with pytest.raises(TypeError):
        # Passing a non-iterable type (e.g., an integer) to the update method should raise a TypeError
        meta_set.update(12345)

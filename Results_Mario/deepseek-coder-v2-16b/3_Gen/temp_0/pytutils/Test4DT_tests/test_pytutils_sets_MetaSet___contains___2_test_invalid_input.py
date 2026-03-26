
import pytest
from pytutils.sets import MetaSet

def test_invalid_input():
    meta_set = MetaSet()
    
    # Test adding an invalid type (e.g., a list) to check error handling
    with pytest.raises(TypeError):
        meta_set.add([1, 2, 3])


import pytest
from flutes.iterator import LazyList

def test_invalid_inputs():
    # Test with invalid inputs like None or a string
    with pytest.raises(TypeError):
        lazy_list = LazyList(None)  # Invalid iterable type

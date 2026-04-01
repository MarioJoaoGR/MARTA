
import pytest
from flutes.iterator import LazyList

def test_none_input():
    with pytest.raises(TypeError):
        lazy_list = LazyList(None)

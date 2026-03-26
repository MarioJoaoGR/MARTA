
import pytest
from flutes.iterator import LazyList

def test_error_case():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(TypeError):
        len(lazy_list)

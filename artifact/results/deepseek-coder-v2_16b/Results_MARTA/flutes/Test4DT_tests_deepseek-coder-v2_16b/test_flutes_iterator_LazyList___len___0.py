
import pytest
from flutes.iterator import LazyList


def test_lazy_list_len_before_exhausted():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(TypeError):
        len(lazy_list)
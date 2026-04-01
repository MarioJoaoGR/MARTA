
import pytest
from flutes.iterator import LazyList

def test_edge_cases():
    my_empty_list = []
    lazy_empty_list = LazyList(my_empty_list)
    none_input = None
    with pytest.raises(TypeError):
        lazy_none_list = LazyList(none_input)

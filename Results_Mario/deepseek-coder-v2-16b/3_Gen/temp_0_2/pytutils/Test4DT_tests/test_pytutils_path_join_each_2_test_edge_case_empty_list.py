
import pytest
from pytutils.path import join_each

def test_edge_case_empty_list():
    parent = "/home/user"
    iterable = []
    
    result = list(join_each(parent, iterable))
    
    assert result == [], "Expected an empty list for an empty iterable"


import pytest
from superstring.superstring import SuperStringSubstring

def test_edge_case():
    base = 'hello'
    start_index = 1
    end_index = 4
    
    ss = SuperStringSubstring(base, start_index, end_index)
    
    assert ss._base == 'hello'
    assert ss._start_index == 1
    assert ss._end_index == 4

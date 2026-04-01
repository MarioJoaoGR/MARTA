
import pytest
from superstring.superstring import SuperStringSubstring

def test_valid_case():
    base = 'hello'
    start_index = 0
    end_index = 5
    
    ss = SuperStringSubstring(base, start_index, end_index)
    
    assert ss._base == 'hello'
    assert ss._start_index == 0
    assert ss._end_index == 5

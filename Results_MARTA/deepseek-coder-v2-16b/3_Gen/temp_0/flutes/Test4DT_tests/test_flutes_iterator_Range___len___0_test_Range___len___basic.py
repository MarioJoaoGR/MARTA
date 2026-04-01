
import pytest
from flutes.iterator import Range

def test_Range___len___basic():
    r = Range(10)
    assert len(r) == 10
    
    r = Range(1, 10 + 1)
    assert len(r) == 10
    
    r = Range(1, 11, 2)
    assert len(r) == 5

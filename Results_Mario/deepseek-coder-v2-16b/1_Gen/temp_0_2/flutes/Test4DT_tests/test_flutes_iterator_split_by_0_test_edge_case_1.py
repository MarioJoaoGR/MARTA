
import pytest
from flutes.iterator import split_by

def test_edge_case_1():
    iterable = []
    empty_segments = False
    criterion = lambda x: True
    
    result = list(split_by(iterable, empty_segments, criterion=criterion))
    
    assert result == [], "Expected an empty list for an empty iterable"

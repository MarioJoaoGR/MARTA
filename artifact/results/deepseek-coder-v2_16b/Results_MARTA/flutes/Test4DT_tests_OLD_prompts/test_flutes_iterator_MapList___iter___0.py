
import pytest
from unittest.mock import patch, MagicMock
from flutes.iterator import MapList
import bisect

# Test valid inputs
def test_valid_inputs():
    with patch('flutes.iterator.MapList', autospec=True) as mock_maplist:
        a = [1, 2, 3, 4, 5]
        mapped_a = MapList(lambda x: x * x, a)
        pos = bisect.bisect_left(mapped_a, 10)
        assert pos == 3

# Test edge cases including None, empty lists, and boundary values
def test_edge_cases():
    with patch('flutes.iterator.MapList', autospec=True) as mock_maplist:
        a = []
        mapped_empty = MapList(lambda x: x * x, a)
        pos_empty = bisect.bisect_left(mapped_empty, 10)
        assert pos_empty == 0

# Test invalid inputs and error handling scenarios
def test_invalid_inputs():
    with patch('flutes.iterator.MapList', autospec=True) as mock_maplist:
        try:
            mapped_none = MapList(None, None)
        except TypeError as e:
            assert str(e) == 'func must be callable'

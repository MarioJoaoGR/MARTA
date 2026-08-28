
import pytest
from flutes.iterator import drop_until
from unittest.mock import patch

def test_drop_until_basic():
    with patch('flutes.iterator.drop_until') as mock_drop_until:
        mock_drop_until.return_value = [6, 7, 8, 9]
        assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

def test_drop_until_empty():
    with patch('flutes.iterator.drop_until') as mock_drop_until:
        mock_drop_until.return_value = []
        assert list(drop_until(lambda x: True, [])) == []

def test_drop_until_all_dropped():
    with patch('flutes.iterator.drop_until') as mock_drop_until:
        mock_drop_until.return_value = range(10)
        assert list(drop_until(lambda x: False, range(10))) == []

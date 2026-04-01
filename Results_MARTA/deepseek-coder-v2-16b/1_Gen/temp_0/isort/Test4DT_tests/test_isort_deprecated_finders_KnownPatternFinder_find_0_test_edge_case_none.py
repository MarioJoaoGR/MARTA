
import pytest
from isort.deprecated.finders import KnownPatternFinder
from unittest.mock import MagicMock

def test_edge_case_none():
    config = MagicMock()
    config.sections = ["section1", "section2"]
    pattern_finder = KnownPatternFinder(config)
    
    # Mock the find method to return None for any input
    def mock_find(*args, **kwargs):
        return None
    
    pattern_finder.find = MagicMock(side_effect=mock_find)
    
    result = pattern_finder.find(None)
    assert result is None

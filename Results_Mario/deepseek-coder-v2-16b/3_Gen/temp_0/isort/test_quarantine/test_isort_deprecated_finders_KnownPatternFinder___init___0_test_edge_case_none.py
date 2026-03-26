
import pytest
from unittest.mock import MagicMock
from isort.deprecated.finders import KnownPatternFinder

def test_edge_case_none():
    # Create a mock Config object with no sections
    config = MagicMock()
    config.sections = []
    
    # Instantiate the KnownPatternFinder with the mock Config
    finder = KnownPatternFinder(config)
    
    # Assert that known_patterns is an empty list
    assert finder.known_patterns == []


import pytest
from unittest.mock import MagicMock
from isort.deprecated.finders import KnownPatternFinder

def test_edge_case():
    # Mock the Config class and its methods
    config = MagicMock()
    config.sections = []  # Empty sections to simulate missing configuration
    config.KNOWN_SECTION_MAPPING = {}  # No section mapping
    config.known_other = {}  # No known patterns in other section
    
    # Instantiate the KnownPatternFinder with the mocked Config
    finder = KnownPatternFinder(config)
    
    # Assert that the known_patterns list is empty as expected for edge case
    assert finder.known_patterns == []

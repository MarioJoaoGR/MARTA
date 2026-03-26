
import pytest
from isort.deprecated.finders import KnownPatternFinder
from unittest.mock import MagicMock

@pytest.fixture
def mock_config():
    config = MagicMock()
    config.sections = []
    config.known_std = []
    config.known_third = []
    return config

def test_edge_case(mock_config):
    finder = KnownPatternFinder(mock_config)
    assert finder.find("nonexistentmodule") is None
    assert finder.find("") is None

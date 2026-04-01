
import pytest
from isort.deprecated.finders import KnownPatternFinder
from unittest.mock import MagicMock

@pytest.fixture
def mock_config():
    config = MagicMock()
    config.sections = ['std', 'third']
    config.known_std = ['module1', 'module2']
    config.known_third = ['module3']
    return config

def test_valid_input(mock_config):
    finder = KnownPatternFinder(mock_config)
    
    # Test with a module name that matches the known patterns
    assert finder.find("module1") == "std"
    assert finder.find("module3") == "third"
    
    # Test with a module name that does not match any known patterns
    assert finder.find("unknown_module") is None

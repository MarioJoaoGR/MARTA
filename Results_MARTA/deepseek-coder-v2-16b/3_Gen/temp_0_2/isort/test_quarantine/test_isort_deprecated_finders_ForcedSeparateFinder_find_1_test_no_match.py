
from isort.deprecated.finders import ForcedSeparateFinder
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def finder():
    config = MagicMock()
    config.forced_separate = ["module1", "module2"]
    return ForcedSeparateFinder(config=config)

def test_find_match(finder):
    assert finder.find("module1") == "module1"

def test_find_no_match(finder):
    assert finder.find("nonexistent_module") is None

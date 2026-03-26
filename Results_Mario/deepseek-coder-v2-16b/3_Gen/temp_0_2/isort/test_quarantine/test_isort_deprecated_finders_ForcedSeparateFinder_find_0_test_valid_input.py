
from isort.deprecated.finders import ForcedSeparateFinder
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def finder():
    config = MagicMock()
    config.forced_separate = ["module1", "module2"]
    return ForcedSeparateFinder(config=config)

def test_find_with_valid_input(finder):
    assert finder.find("module1") == "module1"
    assert finder.find("module2") == "module2"
    assert finder.find("other_module") is None

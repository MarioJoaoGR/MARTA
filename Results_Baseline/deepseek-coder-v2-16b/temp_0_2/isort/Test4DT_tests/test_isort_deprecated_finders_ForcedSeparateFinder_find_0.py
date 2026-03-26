# Module: isort.deprecated.finders
from unittest.mock import MagicMock

import pytest

from isort.deprecated.finders import ForcedSeparateFinder


# Mock Config class and its config attribute for testing
class Config:
    def __init__(self, forced_separate=None):
        self.forced_separate = forced_separate if forced_separate else []

@pytest.fixture
def finder():
    config_instance = Config(forced_separate=["*.utils", "math.*"])
    return ForcedSeparateFinder(config_instance)

# Test cases for the find method
def test_find_existing_pattern(finder):
    module_name = "math.trig"
    result = finder.find(module_name)
    assert result == "math.*"

def test_find_non_existing_pattern(finder):
    module_name = "os.path"
    result = finder.find(module_name)
    assert result is None

def test_find_with_dot_prefix(finder):
    module_name = ".math.trig"
    result = finder.find(module_name)
    assert result == "math.*"

def test_find_empty_forced_separate(finder):
    config_instance = Config(forced_separate=[])
    finder_instance = ForcedSeparateFinder(config_instance)
    module_name = "os.path"
    result = finder_instance.find(module_name)
    assert result is None

def test_find_nonexistent_pattern_with_dot_prefix(finder):
    module_name = ".non_existent_module"
    result = finder.find(module_name)
    assert result is None

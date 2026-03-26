
# Module: isort.deprecated.finders
from re import Pattern

import pytest

from isort import Config


# Fixture to create a default Config object for testing
@pytest.fixture
def default_config():
    return Config()

# Test case for initializing KnownPatternFinder with a default configuration
def test_KnownPatternFinder_default_config(default_config):
    from isort.deprecated.finders import \
        KnownPatternFinder  # Importing here to fix the undefined variable error
    pattern_finder = KnownPatternFinder(config=default_config)
    assert isinstance(pattern_finder.known_patterns, list), "Expected known_patterns to be a list"
    assert all(isinstance(item, tuple) and len(item) == 2 for item in pattern_finder.known_patterns), \
        "Each item in known_patterns should be a tuple of (Pattern[str], str)"
    assert all(isinstance(pattern, Pattern) and isinstance(section, str) for pattern, section in pattern_finder.known_patterns), \
        "The first element of each tuple should be a compiled regex pattern, and the second element should be a string"

# Test case for initializing KnownPatternFinder with a custom configuration file
@pytest.mark.parametrize("settings_file", ["path/to/custom_config.toml"])
def test_KnownPatternFinder_custom_config(settings_file):
    from isort.deprecated.finders import \
        KnownPatternFinder  # Importing here to fix the undefined variable error
    with pytest.raises(FileNotFoundError):  # Simulate file not found error for custom config
        pattern_finder = KnownPatternFinder(config=Config(settings_file=settings_file))

# Test case for initializing KnownPatternFinder with an overridden configuration
@pytest.mark.parametrize("config_overrides", [{"quiet": True}])
def test_KnownPatternFinder_overridden_config(default_config, config_overrides):
    from isort.deprecated.finders import \
        KnownPatternFinder  # Importing here to fix the undefined variable error
    new_config = Config(config=default_config, **config_overrides)
    pattern_finder = KnownPatternFinder(config=new_config)
    assert isinstance(pattern_finder.known_patterns, list), "Expected known_patterns to be a list"
    assert all(isinstance(item, tuple) and len(item) == 2 for item in pattern_finder.known_patterns), \
        "Each item in known_patterns should be a tuple of (Pattern[str], str)"
    assert all(isinstance(pattern, Pattern) and isinstance(section, str) for pattern, section in pattern_finder.known_patterns), \
        "The first element of each tuple should be a compiled regex pattern, and the second element should be a string"


# Module: isort.deprecated.finders
import pytest
from isort import Config
from re import Pattern

# Fixture to create a default Config object for testing
@pytest.fixture
def default_config():
    return Config()

# Test case to initialize KnownPatternFinder with a default configuration
def test_init_with_default_config(default_config):
    from isort.finders import KnownPatternFinder  # Importing the class here fixes the undefined variable error
    pattern_finder = KnownPatternFinder(config=default_config)
    assert isinstance(pattern_finder, KnownPatternFinder)
    assert isinstance(pattern_finder.known_patterns, list)
    assert all(isinstance(pattern, tuple) and len(pattern) == 2 for pattern in pattern_finder.known_patterns)
    assert all(isinstance(compiled_pattern, Pattern) and isinstance(section_name, str) for compiled_pattern, section_name in pattern_finder.known_patterns)

# Test case to initialize KnownPatternFinder with a custom configuration file
def test_init_with_custom_config():
    from isort.finders import KnownPatternFinder  # Importing the class here fixes the undefined variable error
    settings_file = 'path/to/custom_config.toml'
    config = Config(settings_file=settings_file)
    pattern_finder = KnownPatternFinder(config=config)
    assert isinstance(pattern_finder, KnownPatternFinder)
    assert isinstance(pattern_finder.known_patterns, list)
    assert all(isinstance(pattern, tuple) and len(pattern) == 2 for pattern in pattern_finder.known_patterns)
    assert all(isinstance(compiled_pattern, Pattern) and isinstance(section_name, str) for compiled_pattern, section_name in pattern_finder.known_patterns)

# Test case to initialize KnownPatternFinder with an existing configuration
def test_init_with_existing_config():
    from isort.finders import KnownPatternFinder  # Importing the class here fixes the undefined variable error
    existing_config = Config()
    new_config = Config(config=existing_config, quiet=True)
    pattern_finder = KnownPatternFinder(config=new_config)
    assert isinstance(pattern_finder, KnownPatternFinder)
    assert isinstance(pattern_finder.known_patterns, list)
    assert all(isinstance(pattern, tuple) and len(pattern) == 2 for pattern in pattern_finder.known_patterns)
    assert all(isinstance(compiled_pattern, Pattern) and isinstance(section_name, str) for compiled_pattern, section_name in pattern_finder.known_patterns)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_KnownPatternFinder___init___0
isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0.py:14:4: E0401: Unable to import 'isort.finders' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0.py:14:4: E0611: No name 'finders' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0.py:23:4: E0401: Unable to import 'isort.finders' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0.py:23:4: E0611: No name 'finders' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0.py:34:4: E0401: Unable to import 'isort.finders' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0.py:34:4: E0611: No name 'finders' in module 'isort' (no-name-in-module)


"""
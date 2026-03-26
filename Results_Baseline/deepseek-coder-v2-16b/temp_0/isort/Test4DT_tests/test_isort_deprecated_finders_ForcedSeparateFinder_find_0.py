
import pytest

from isort.deprecated.finders import ForcedSeparateFinder


# Create an instance of ForcedSeparateFinder with a mock config
@pytest.fixture
def finder():
    class MockConfig:
        forced_separate = []
    
    return ForcedSeparateFinder(config=MockConfig())

# Test cases for find method
def test_find_with_matching_pattern(finder):
    # Given a module name that matches one of the forced separate patterns
    finder.config.forced_separate = ["some"]
    result = finder.find("some_module")
    # Then it should return the matching pattern
    assert result == "some"

def test_find_without_matching_pattern(finder):
    # Given a module name that does not match any of the forced separate patterns
    finder.config.forced_separate = ["first", "second"]
    result = finder.find("unrelated_module")
    # Then it should return None
    assert result is None

def test_find_with_wildcard_in_pattern(finder):
    # Given a module name that matches one of the forced separate patterns with wildcard
    finder.config.forced_separate = ["another*"]
    result = finder.find("another_module")
    # Then it should return the matching pattern
    assert result == "another*"

def test_find_with_dot_prefix(finder):
    # Given a module name that starts with a dot and matches one of the forced separate patterns
    finder.config.forced_separate = ["some*"]
    result = finder.find(".some_module")
    # Then it should return the matching pattern
    assert result == "some*"

def test_find_with_multiple_patterns(finder):
    # Given a module name that matches multiple forced separate patterns
    finder.config.forced_separate = ["first", "second"]
    result1 = finder.find("first_module")
    result2 = finder.find("second_module")
    # Then it should return the first matching pattern or None if no match is found
    assert result1 == "first"
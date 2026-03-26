# Module: flutes.fs
import pytest
from flutes.fs import remove_suffix

# Test cases for remove_suffix function

def test_remove_fully_matching_suffix():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"

def test_remove_non_fully_matching_suffix():
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"

def test_default_usage():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"

def test_non_fully_matching_suffix_default_fully_match():
    assert remove_suffix("bugfix", "fix") == "bug"

# Additional edge cases to consider:

def test_remove_empty_string():
    assert remove_suffix("", "") == ""

def test_remove_no_suffix():
    assert remove_suffix("https://github.com/huzecong", "/flutes") == "https://github.com/huzecong"

def test_remove_longer_suffix():
    assert remove_suffix("bugfix", "bug") == "bugfix"  # The suffix is longer than the string, so it should not be removed.

def test_remove_non_matching_suffix():
    assert remove_suffix("https://github.com/huzecong/flutes", "/example") == "https://github.com/huzecong/flutes"  # The suffix does not match, so the string should remain unchanged.

def test_remove_suffix_with_fully_match_false():
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"

def test_remove_suffix_with_fully_match_true():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"

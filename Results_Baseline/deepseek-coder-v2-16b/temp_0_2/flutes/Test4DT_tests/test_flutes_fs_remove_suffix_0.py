
import pytest
from flutes.fs import remove_suffix

# Test cases for remove_suffix function
def test_remove_suffix_fully_matching():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"

def test_remove_suffix_non_fully_matching():
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"

def test_remove_suffix_empty_string():
    assert remove_suffix("", "suffix") == ""

def test_remove_suffix_partially_matching():
    assert remove_suffix("https://github.com/huzecong/flutes/", "/") == "https://github.com/huzecong/flutes"

# Additional edge cases to consider
def test_remove_suffix_no_suffix_to_remove():
    assert remove_suffix("no suffix here", "extra") == "no suffix here"

def test_remove_suffix_fully_match_false_with_exact_match():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes", fully_match=False) == "https://github.com/huzecong"

def test_remove_suffix_fully_match_true_no_match():
    assert remove_suffix("https://github.com/huzecong/flutes", "/extra") == "https://github.com/huzecong/flutes"

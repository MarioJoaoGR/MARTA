
import pytest
from flutes.fs import remove_prefix

# Test cases for remove_prefix function
def test_remove_prefix_fully_matching():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://") == "github.com/huzecong/flutes"

def test_remove_prefix_non_fully_matching():
    assert remove_prefix("preface", "pre", fully_match=False) == "face"

def test_remove_prefix_not_fully_matching_default():
    assert remove_prefix("preface", "pre") == "face"

def test_remove_prefix_no_match():
    assert remove_prefix("hello world", "he") == "llo world"

# Edge case tests for empty string and different prefixes
def test_remove_prefix_fully_matching_empty_string():
    assert remove_prefix("", "https://") == ""

def test_remove_prefix_non_fully_matching_with_longer_prefix():
    assert remove_prefix("preface", "prex") == "preface"

# Test cases for fully_match=False and partial prefix match
def test_remove_prefix_partial_match():
    assert remove_prefix("http://example.com", "http:") == "//example.com"

def test_remove_prefix_fully_match_false_no_match():
    assert remove_prefix("hello", "el") == "hello"

# Test cases for different input strings and prefixes
def test_remove_prefix_different_input_string():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://") == "github.com/huzecong/flutes"

def test_remove_prefix_different_prefix():
    assert remove_prefix("hello world", "hell") == "o world"

# Test cases for edge cases with empty strings and prefixes
def test_remove_prefix_empty_string_and_non_empty_prefix():
    assert remove_prefix("", "https://") == ""

def test_remove_prefix_non_empty_string_and_empty_prefix():
    assert remove_prefix("hello world", "") == "hello world"

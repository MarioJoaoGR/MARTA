
# Module: isort._vendored.tomli._parser
import pytest
from isort._vendored.tomli._parser import skip_chars, Pos
from typing import Iterable

# Helper function to create a custom position object for testing
def make_pos(value):
    class CustomPos(Pos):
        def __getitem__(self, index):
            return value + index
        def __iadd__(self, other):
            return CustomPos(self.value + other)
    
    # Adding a 'value' attribute to the CustomPos class
    CustomPos.__init__ = lambda self, value: setattr(self, 'value', value)
    
    return CustomPos(value)

# Test cases for skip_chars function
def test_skip_chars_basic():
    src = "hello"
    pos = 0
    chars_to_skip = ['l']
    result = skip_chars(src, make_pos(pos), chars_to_skip)
    assert result == 4, f"Expected position after skipping 'l' to be 4, but got {result}"

def test_skip_chars_start_from_middle():
    src = "hello"
    pos = 2
    chars_to_skip = ['o']
    result = skip_chars(src, make_pos(pos), chars_to_skip)
    assert result == 5, f"Expected position after skipping 'o' to be 5, but got {result}"

def test_skip_chars_multiple_chars():
    src = "mississippi"
    pos = 1
    chars_to_skip = ['i', 's']
    result = skip_chars(src, make_pos(pos), chars_to_skip)
    assert result == 8, f"Expected position after skipping all 'i' and 's' to be 8, but got {result}"

def test_skip_chars_all_chars():
    src = "abcdef"
    pos = 3
    chars_to_skip = ['a', 'b', 'c', 'd', 'e', 'f']
    result = skip_chars(src, make_pos(pos), chars_to_skip)
    assert result == 6, f"Expected position after skipping all characters to be 6, but got {result}"

def test_skip_chars_index_error():
    src = "hello"
    pos = 5
    chars_to_skip = ['l']
    result = skip_chars(src, make_pos(pos), chars_to_skip)
    assert result == 5, f"Expected position to remain unchanged at 5 after IndexError, but got {result}"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_skip_chars_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0.py:13:29: E1101: Instance of 'CustomPos' has no 'value' member (no-member)


"""

import pytest
from apimd.parser import doctest

# Test for valid input with happy path

# Test for invalid input where the function should raise a TypeError

# Test for empty string input
def test_empty_string_input():
    doc = ""
    expected_output = ""
    assert doctest(doc) == expected_output

# Test for a single line that does not start with ">>>"
def test_single_line_no_triple_quotes():
    doc = "This is a normal line."
    expected_output = "This is a normal line."
    assert doctest(doc) == expected_output

# Test for multiple lines where some start with ">>>" and others do not
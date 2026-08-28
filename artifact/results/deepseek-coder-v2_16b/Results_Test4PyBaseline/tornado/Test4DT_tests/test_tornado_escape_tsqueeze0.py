# Module: tornado.escape
import pytest
import re
from tornado.escape import squeeze

# Test cases for the squeeze function
def test_squeeze_basic():
    assert squeeze("Hello   world!") == 'Hello world!'

def test_squeeze_with_leading_trailing_whitespace():
    assert squeeze("  This is a test.  ") == 'This is a test.'

def test_squeeze_multiple_whitespace_characters():
    assert squeeze("Multiple \n\t spaces are replaced.") == 'Multiple spaces are replaced.'

# Additional edge cases to consider:
def test_squeeze_empty_string():
    assert squeeze("") == ''

def test_squeeze_no_whitespace():
    assert squeeze("NoSpaces") == 'NoSpaces'

def test_squeeze_only_whitespace():
    assert squeeze("   ") == ''

# Test case for handling different whitespace characters
def test_squeeze_different_whitespace_characters():
    assert squeeze("Tabs\tand\nnewlines\fare replaced.") == 'Tabs and newlines are replaced.'

# Test case to ensure the function handles mixed content correctly
def test_squeeze_mixed_content():
    assert squeeze("Hello   world! This is a test.") == 'Hello world! This is a test.'

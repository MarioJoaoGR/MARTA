
import re
import pytest
from tornado.escape import squeeze

def test_squeeze_multiple_spaces():
    assert squeeze("Hello   world!") == "Hello world!"

def test_squeeze_leading_trailing_whitespace():
    assert squeeze("  This is a test.  ") == "This is a test."

def test_squeeze_multiple_control_chars():
    assert squeeze("Multiple \n\t spaces") == "Multiple spaces"

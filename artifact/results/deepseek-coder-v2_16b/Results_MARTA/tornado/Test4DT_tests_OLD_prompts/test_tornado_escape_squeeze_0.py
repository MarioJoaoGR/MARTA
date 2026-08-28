
import pytest
from unittest.mock import patch
from tornado.escape import squeeze


def test_empty_string():
    assert squeeze("") == ""


def test_multiple_spaces():
    assert squeeze("Hello   world!") == "Hello world!"

def test_leading_trailing_spaces():
    assert squeeze("  This is a test.  ") == "This is a test."

def test_multiple_whitespace_chars():
    assert squeeze("Multiple \n\t spaces") == "Multiple spaces"
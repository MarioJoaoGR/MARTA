# Module: isort.format
import pytest
from isort.format import remove_whitespace

def test_remove_whitespace_basic():
    assert remove_whitespace("Hello World") == "HelloWorld"

def test_remove_whitespace_custom_line_separator():
    assert remove_whitespace("Line1\nLine2", line_separator="\n") == "Line1Line2"

def test_remove_whitespace_form_feed_separator():
    assert remove_whitespace("Page\x0cBreak", line_separator="\x0c") == "PageBreak"

def test_remove_whitespace_multiple_whitespace_types():
    assert remove_whitespace("  Line1 \nLine2 \x0c Line3  ") == "Line1Line2Line3"

def test_remove_whitespace_no_whitespace():
    assert remove_whitespace("NoWhitespaceHere") == "NoWhitespaceHere"

def test_remove_whitespace_only_whitespace():
    assert remove_whitespace("   \n\x0c  ") == ""

def test_remove_whitespace_empty_string():
    assert remove_whitespace("") == ""

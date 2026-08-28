
import pytest
from isort.format import remove_whitespace



def test_custom_line_separator():
    input_string = "Line1\nLine2"
    line_separator = "\n"
    expected_output = "Line1Line2"
    assert remove_whitespace(input_string, line_separator=line_separator) == expected_output

def test_form_feed_character():
    input_string = "Page\x0cBreak"
    line_separator = "\x0c"
    expected_output = "PageBreak"
    assert remove_whitespace(input_string, line_separator=line_separator) == expected_output

def test_no_whitespace():
    input_string = "NoWhitespaceHere"
    expected_output = "NoWhitespaceHere"
    assert remove_whitespace(input_string) == expected_output


def test_single_line_with_spaces():
    input_string = " Single Line With Spaces "
    expected_output = "SingleLineWithSpaces"
    assert remove_whitespace(input_string) == expected_output

def test_multiple_newlines():
    input_string = "\n\nMultiple\nNewlines\n\n"
    expected_output = "MultipleNewlines"
    assert remove_whitespace(input_string) == expected_output
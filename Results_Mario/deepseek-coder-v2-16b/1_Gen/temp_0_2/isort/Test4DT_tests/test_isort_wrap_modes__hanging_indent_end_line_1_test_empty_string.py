
import pytest
from isort.wrap_modes import _hanging_indent_end_line

def test__hanging_indent_end_line():
    # Test when line ends with a space
    assert _hanging_indent_end_line("This is a test line.") == "This is a test line. \\"
    
    # Test when line does not end with a space
    assert _hanging_indent_end_line("Another example line, with more text.") == "Another example line, with more text. \\"
    
    # Test an empty string (should add a space and backslash)
    assert _hanging_indent_end_line("") == " \\"

# Module: isort.wrap_modes
# test_wrap_modes.py
from isort.wrap_modes import _hanging_indent_end_line


def test_hanging_indent_end_line():
    # Test case 1: Line does not end with a space, should add a space and backslash
    assert _hanging_indent_end_line("This is a test line.") == 'This is a test line. \\'
    
    # Test case 2: Line already ends with a space, no change should be made
    assert _hanging_indent_end_line("Another example, with more words. ") == 'Another example, with more words. \\'
    
    # Test case 3: Empty line, should add a space and backslash
    assert _hanging_indent_end_line("") == " \\"
    
    # Test case 4: Line ending with another character than a space, should add a space and backslash
    assert _hanging_indent_end_line("This is not a spaced line!") == 'This is not a spaced line! \\'


# Importing necessary modules from isort for testing purposes
from isort.wrap_modes import _hanging_indent_end_line  # Corrected import path

def test_valid_input():
    assert _hanging_indent_end_line("This is a test line.") == "This is a test line. \\"
    assert _hanging_indent_end_line("Another example line, with more text.") == "Another example line, with more text. \\"

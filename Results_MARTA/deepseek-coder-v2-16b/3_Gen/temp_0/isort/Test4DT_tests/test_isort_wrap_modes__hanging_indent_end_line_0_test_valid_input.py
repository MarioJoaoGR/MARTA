
import pytest

from isort.wrap_modes import _hanging_indent_end_line


def test_valid_input():
    assert _hanging_indent_end_line("This is a test line.") == "This is a test line. \\"
    assert _hanging_indent_end_line("Another example, with more words.") == "Another example, with more words. \\"


import pytest
from unittest.mock import patch
from isort.core import _has_changed  # Assuming this module and function exist

@pytest.mark.parametrize("before, after, ignore_whitespace, expected", [
    ("Hello, World!", "Hello, World!", False, False),
    ("This is a test.\nWith new lines.", "This is a test.\nWith different lines.", False, True),
    ("  No changes here  ", "No changes here", False, False),
    ("Content with spaces.", "Content with spaces.", True, False),
])
def test_has_changed(before, after, ignore_whitespace, expected):
    assert _has_changed(before, after, line_separator="\n", ignore_whitespace=ignore_whitespace) == expected

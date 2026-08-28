
import pytest
from isort.format import remove_whitespace

def test_remove_whitespace():
    # Test removing whitespace characters including spaces, form feeds, and line separators
    content = "Hello, World!"
    expected_output = "Hello,World!"
    assert remove_whitespace(content) == expected_output



import pytest

from isort._vendored.tomli._parser import skip_comments_and_array_ws

# Define the TOML_WS_AND_NEWLINE constant as per the function's requirements
TOML_WS_AND_NEWLINE = " \t\n"  # Assuming this is the set of whitespace characters defined in the module

def test_skip_comments_and_array_ws_simple():
    src = "   # This is a comment\nint x = 10;"
    pos = 0
    result = skip_comments_and_array_ws(src, pos)
    assert result == 23, f"Expected position after skipping to be 23, but got {result}"

def test_skip_comments_and_array_ws_complex():
    src = "   \t# This is another comment\nimport os\n# Another comment here\nprint('Hello, World!');"
    pos = 0
    result = skip_comments_and_array_ws(src, pos)

import pytest
from thefuck.rules.cat_dir import get_new_command
from thefuck.types import Command

# Test cases for get_new_command function
@pytest.mark.parametrize("input_command, expected", [
    ("cat file1", "ls file1"),  # Basic usage
    ("no change needed here", "no change needed here"),  # No change needed
    ("cat cat cat", "ls cat cat"),  # Multiple replacements
    ("", ""),  # Edge case - empty string
])
def test_get_new_command(input_command, expected):
    assert get_new_command(Command(input_command, "")) == expected

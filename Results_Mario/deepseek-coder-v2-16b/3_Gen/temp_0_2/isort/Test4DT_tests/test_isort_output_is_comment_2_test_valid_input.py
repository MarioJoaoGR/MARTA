
import pytest

def is_comment(line: str | None) -> bool:
    return line.startswith("#") if line else False

@pytest.mark.parametrize("line, expected", [
    ("# This is a comment # This is not visible", True),
    ("This is not a comment", False),
    (None, False),
    ("# This is a hidden comment", True)
])
def test_valid_input(line, expected):
    assert is_comment(line) == expected

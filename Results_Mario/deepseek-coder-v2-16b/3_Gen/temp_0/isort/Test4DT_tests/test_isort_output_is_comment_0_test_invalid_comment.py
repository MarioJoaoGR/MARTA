
import pytest

def is_comment(line: str | None) -> bool:
    return line.startswith("#") if line else False

@pytest.mark.parametrize("line, expected", [
    ('This is not a comment', False),
    (None, False),
    ('# This is a comment', True),
])
def test_invalid_comment(line, expected):
    assert is_comment(line) == expected

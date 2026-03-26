
import pytest
from isort.comments import parse

def add_to_line(
    comments: list[str] | None,
    original_string: str = "",
    removed: bool = False,
    comment_prefix: str = "",
) -> str:
    """Returns a string with comments added if removed is not set."""
    if removed:
        return parse(original_string)[0]

    if not comments:
        return original_string

    unique_comments: list[str] = []
    for comment in comments:
        if comment not in unique_comments:
            unique_comments.append(comment)
    return f"{parse(original_string)[0]}{comment_prefix} {'; '.join(unique_comments)}"

def test_removed_true():
    assert add_to_line(['This is comment 1', 'This is comment 2'], "import os", removed=True) == "import os"
    assert add_to_line(None, "print('Hello, World!')", removed=True) == "print('Hello, World!')"
    assert add_to_line(['This is comment 1', 'This is comment 2'], "import os", removed=True) == "import os"

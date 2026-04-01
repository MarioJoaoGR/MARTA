
import pytest
from isort.comments import parse  # Assuming this module exists for parsing comments

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

def test_none_input():
    original_string = "import os"
    comments = None
    removed = False
    comment_prefix = "#"
    
    result = add_to_line(comments, original_string, removed, comment_prefix)
    
    assert result == original_string

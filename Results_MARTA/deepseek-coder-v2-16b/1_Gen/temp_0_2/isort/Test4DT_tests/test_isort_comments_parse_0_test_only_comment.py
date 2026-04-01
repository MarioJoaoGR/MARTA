
import pytest

def parse(line: str) -> tuple[str, str]:
    """Parses import lines for comments and returns back the
    import statement and the associated comment.
    """
    comment_start = line.find("#")
    if comment_start != -1:
        return (line[:comment_start], line[comment_start + 1 :].strip())

    return (line, "")

def test_only_comment():
    line = '# This is a comment, not an import statement'
    result = parse(line)
    assert result == ('', 'This is a comment, not an import statement')

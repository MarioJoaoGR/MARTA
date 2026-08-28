
from docstring_parser import parse  # Importing the parse function

def test_parse_with_examples():
    text = """Short description.

Examples:
    >>> add(2, 3)
    5
    >>> add(-1, -1)
    -2"""
    doc = parse(text)
    assert doc.short_description == "Short description."
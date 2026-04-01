
import pytest
from docstring_parser.numpydoc import Section

@pytest.mark.parametrize("title, key", [
    ("Parameters", "params"),
    ("Attributes", "attrs"),
    ("Returns", "returns"),
    ("Raises", "raises"),
    ("Example", "example")
])
def test_valid_input(title, key):
    section = Section(title=title, key=key)
    assert section.title == title
    assert section.key == key

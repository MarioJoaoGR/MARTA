
import pytest
from docstring_parser.numpydoc import Section, DocstringMeta
import re  # Importing re module for regular expression operations

# Test creating a Section object with specific title and key
def test_section_creation():
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
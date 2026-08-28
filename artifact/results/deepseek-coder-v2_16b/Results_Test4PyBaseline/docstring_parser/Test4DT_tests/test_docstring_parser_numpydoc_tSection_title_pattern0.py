
import pytest
from docstring_parser.numpydoc import Section
import re  # Importing re module for regular expression operations

# Test initialization of Section with different titles and keys
def test_section_initialization():
    section_params = Section(title="Parameters", key="params")
    assert section_params.title == "Parameters"
    assert section_params.key == "params"

    section_returns = Section(title="Returns", key="returns")
    assert section_returns.title == "Returns"
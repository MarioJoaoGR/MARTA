
import pytest
from docstring_parser.numpydoc import Section

@pytest.fixture
def section():
    return Section(title="Parameters", key="params")

def test_section_initialization(section):
    assert section.title == "Parameters"
    assert section.key == "params"

def test_section_str_representation(section):
    expected_str = f"Section({repr('Parameters')}, {repr('params')})"
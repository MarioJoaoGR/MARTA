
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section, DEFAULT_SECTIONS

@pytest.mark.parametrize("invalid_section", [
    {"title": "Parameters", "title_pattern": r'^Parameters$', "key": None},  # Invalid key argument
])
def test_add_section_invalid_input(invalid_section):
    parser = NumpydocParser()
    with pytest.raises(TypeError):
        parser.add_section(section=Section(**invalid_section))

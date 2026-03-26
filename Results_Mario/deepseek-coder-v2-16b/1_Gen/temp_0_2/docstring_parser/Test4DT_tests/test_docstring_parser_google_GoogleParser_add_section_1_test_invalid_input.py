
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_invalid_input():
    parser = GoogleParser()
    
    # Attempt to add an invalid section type
    with pytest.raises(TypeError):
        parser.add_section(Section("InvalidType", "content"))

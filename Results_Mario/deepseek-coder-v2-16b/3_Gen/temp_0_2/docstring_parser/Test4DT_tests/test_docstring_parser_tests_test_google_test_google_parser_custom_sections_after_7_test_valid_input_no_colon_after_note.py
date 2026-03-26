
import pytest
from docstring_parser.tests.test_google import GoogleParser, Section, SectionType

def test_valid_input_no_colon_after_note() -> None:
    parser = GoogleParser(title_colon=False)
    parser.add_section(Section("Note", "note", SectionType.SINGULAR))
    
    docstring = parser.parse(
        """
        short description

        Note:
            a note
        """)
    assert docstring.short_description == "short description"
    assert docstring.long_description == "Note:\n    a note"

    docstring = parser.parse(
        """
        short description

        Note a note
        """)
    assert docstring.short_description == "short description"
    assert docstring.long_description == "Note a note"

    docstring = parser.parse(
        """
        short description

        Note
            a note
        """)
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["note"]
    assert docstring.meta[0].description == "a note"

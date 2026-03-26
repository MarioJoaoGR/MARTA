
from docstring_parser.tests.test_google import GoogleParser, SectionType

def test_google_parser_custom_sections_after() -> None:
    """Test parsing an unknown section with custom GoogleParser configuration
    that was set at a runtime.
    """
    parser = GoogleParser(title_colon=False)
    parser.add_section(Section("Note", "note", SectionType.SINGULAR))
    docstring = parser.parse(
        """
        short description

        Note:
            a note
        """
    )
    assert docstring.short_description == "short description"
    assert docstring.long_description == "Note:\n    a note"

    docstring = parser.parse(
        """
        short description

        Note a note
        """
    )
    assert docstring.short_description == "short description"
    assert docstring.long_description == "Note a note"

    docstring = parser.parse(
        """
        short description

        Note
            a note
        """
    )
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["note"]
    assert docstring.meta[0].description == "a note"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_google_parser_custom_sections_after_2_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_custom_sections_after_2_test_invalid_input.py:9:23: E0602: Undefined variable 'Section' (undefined-variable)

"""

import pytest
from docstring_parser import google
from docstring_parser.common import SectionType

def test_google_parser_parse_valid_input():
    # Arrange
    parser = google.GoogleParser()
    
    # Act
    parsed_docstring = parser.parse("""
    A brief description.
    
    Longer description that spans multiple lines.
    
    Args:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
    
    Returns:
        ReturnType: Description of the return value.
    """)
    
    # Assert
    assert parsed_docstring is not None
    assert len(parsed_docstring.meta) == 2
    assert all(isinstance(section, google.Section) for section in parsed_docstring.meta)
    args_section = next((section for section in parsed_docstring.meta if section.title == 'Args'), None)
    returns_section = next((section for section in parsed_docstring.meta if section.title == 'Returns'), None)
    assert args_section is not None
    assert returns_section is not None
    assert args_section.type == SectionType.MULTIPLE
    assert returns_section.type == SectionType.SINGULAR

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_GoogleParser_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_0_test_valid_input.py:4:0: E0611: No name 'SectionType' in module 'docstring_parser.common' (no-name-in-module)


"""
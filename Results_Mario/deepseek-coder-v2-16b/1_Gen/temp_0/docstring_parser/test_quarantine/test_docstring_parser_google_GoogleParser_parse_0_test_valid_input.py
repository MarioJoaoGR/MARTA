
import pytest
from docstring_parser.google import GoogleParser
from docstring_parser.sections import Section, DEFAULT_SECTIONS
from docstring_parser.docstrings import Docstring, DocstringStyle
from docstring_parser.exceptions import ParseError

def test_valid_input():
    """Test that the GoogleParser can parse a valid input correctly."""
    # Define some sections
    sec1 = Section("Args", "These are the arguments.")
    sec2 = Section("Returns", "This is what it returns.")
    
    # Create a parser with custom sections and title colon disabled
    parser = GoogleParser([sec1, sec2], title_colon=False)
    
    # Define a sample docstring
    docstring_text = """
    A simple example function.
    
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
        
    Returns:
        int: The result of the computation.
    """
    
    # Parse the docstring
    parsed_docstring = parser.parse(docstring_text)
    
    # Check that the parsed docstring has the correct sections and content
    assert parsed_docstring.short_description == "A simple example function."
    assert len(parsed_docstring.meta) == 2
    assert all(isinstance(m, dict) for m in parsed_docstring.meta)
    
    # Check the first argument section
    args_section = next((s for s in parsed_docstring.meta if s['title'] == 'Args'), None)
    assert args_section is not None
    assert args_section['content'] == "param1 (int): The first parameter.\nparam2 (str): The second parameter."
    
    # Check the returns section
    returns_section = next((s for s in parsed_docstring.meta if s['title'] == 'Returns'), None)
    assert returns_section is not None
    assert returns_section['content'] == "int: The result of the computation."
    
    # Check that there are no colons after section titles
    assert all(not s['title'].endswith(':') for s in parsed_docstring.meta)

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_GoogleParser_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_0_test_valid_input.py:4:0: E0401: Unable to import 'docstring_parser.sections' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_0_test_valid_input.py:4:0: E0611: No name 'sections' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_0_test_valid_input.py:5:0: E0401: Unable to import 'docstring_parser.docstrings' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_0_test_valid_input.py:5:0: E0611: No name 'docstrings' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_0_test_valid_input.py:6:0: E0401: Unable to import 'docstring_parser.exceptions' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_0_test_valid_input.py:6:0: E0611: No name 'exceptions' in module 'docstring_parser' (no-name-in-module)

"""
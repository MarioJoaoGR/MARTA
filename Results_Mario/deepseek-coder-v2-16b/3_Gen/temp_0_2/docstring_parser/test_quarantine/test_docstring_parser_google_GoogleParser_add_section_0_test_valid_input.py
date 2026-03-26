
from docstring_parser.google import GoogleParser, Section, SectionType

def test_add_section():
    """Test adding a new section to GoogleParser."""
    
    # Create an instance of GoogleParser with default settings
    parser = GoogleParser()
    
    # Define the new section
    new_section = Section(title="Note", content="note", type=SectionType.SINGULAR)
    
    # Add the new section to the parser
    parser.add_section(new_section)
    
    # Assert that the new section is added correctly
    assert "Note" in parser.sections
    assert parser.sections["Note"].content == "note"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_add_section_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_add_section _______________________________

    def test_add_section():
        """Test adding a new section to GoogleParser."""
    
        # Create an instance of GoogleParser with default settings
        parser = GoogleParser()
    
        # Define the new section
>       new_section = Section(title="Note", content="note", type=SectionType.SINGULAR)
E       TypeError: SectionBase.__new__() got an unexpected keyword argument 'content'

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_add_section_0_test_valid_input.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_add_section_0_test_valid_input.py::test_add_section
============================== 1 failed in 0.03s ===============================
"""
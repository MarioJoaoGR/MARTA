
import pytest
from docstring_parser.google import GoogleParser, Section, SectionType

def test_google_parser_custom_sections():
    parser = GoogleParser(
        [
            Section("DESCRIPTION", "desc", SectionType.SINGULAR),
            Section("ARGUMENTS", "param", SectionType.MULTIPLE),
            Section("ATTRIBUTES", "attribute", SectionType.MULTIPLE),
            Section("EXAMPLES", "examples", SectionType.SINGULAR),
        ],
        title_colon=False,
    )
    docstring = parser.parse(
        """
        DESCRIPTION: This is the description.
    
        ARGUMENTS
            arg1: first arg
            arg2: second arg
    
        ATTRIBUTES
            attr1: first attribute
            attr2: second attribute
    
        EXAMPLES
            Many examples
            More examples
        """
    )
    
    assert docstring.short_description is None
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_custom_sections_1.py F [100%]

=================================== FAILURES ===================================
______________________ test_google_parser_custom_sections ______________________

    def test_google_parser_custom_sections():
        parser = GoogleParser(
            [
                Section("DESCRIPTION", "desc", SectionType.SINGULAR),
                Section("ARGUMENTS", "param", SectionType.MULTIPLE),
                Section("ATTRIBUTES", "attribute", SectionType.MULTIPLE),
                Section("EXAMPLES", "examples", SectionType.SINGULAR),
            ],
            title_colon=False,
        )
        docstring = parser.parse(
            """
            DESCRIPTION: This is the description.
    
            ARGUMENTS
                arg1: first arg
                arg2: second arg
    
            ATTRIBUTES
                attr1: first attribute
                attr2: second attribute
    
            EXAMPLES
                Many examples
                More examples
            """
        )
    
>       assert docstring.short_description is None
E       AssertionError: assert 'DESCRIPTION: This is the description.' is None
E        +  where 'DESCRIPTION: This is the description.' = <docstring_parser.common.Docstring object at 0x102235870>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_custom_sections_1.py:33: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_custom_sections_1.py::test_google_parser_custom_sections
============================== 1 failed in 0.02s ===============================

"""
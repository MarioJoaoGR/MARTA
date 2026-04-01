
from docstring_parser.tests.test_google import parse

def test_empty_example() -> None:
    """Test parsing empty examples section."""
    docstring = parse(
        """Short description

        Example:

        Raises:
            IOError: some error
        """
    )

    assert len(docstring.examples) == 0

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_empty_example_0_test_missing_lines.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_example ______________________________

    def test_empty_example() -> None:
        """Test parsing empty examples section."""
        docstring = parse(
            """Short description
    
            Example:
    
            Raises:
                IOError: some error
            """
        )
    
>       assert len(docstring.examples) == 0
E       assert 1 == 0
E        +  where 1 = len([<docstring_parser.common.DocstringExample object at 0x102237f40>])
E        +    where [<docstring_parser.common.DocstringExample object at 0x102237f40>] = <docstring_parser.common.Docstring object at 0x102237c10>.examples

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_empty_example_0_test_missing_lines.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_empty_example_0_test_missing_lines.py::test_empty_example
============================== 1 failed in 0.03s ===============================

"""

import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_returns() -> None:
    """Test parsing returns."""
    # Test when docstring is None
    docstring = parse(None)
    assert docstring is None

    # Test when there's no return section in the docstring
    docstring = parse("Short description")
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test single return type with no description
    docstring = parse("""
        Short description
        Returns
        -------
        int
    """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test single return type with description
    docstring = parse("""
        Short description
        Returns
        -------
        int
            description
    """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test multiple return types in one block with descriptions
    docstring = parse("""
        Short description
        Returns
        -------
        int
            description for a
        str
            description for b
    """)
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name == "int"
    assert docstring.many_returns[0].description == "description for a"
    assert docstring.many_returns[1].type_name == "str"
    assert docstring.many_returns[1].description == "description for b"

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_returns_3_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_returns _________________________________

    def test_returns() -> None:
        """Test parsing returns."""
        # Test when docstring is None
        docstring = parse(None)
>       assert docstring is None
E       assert <docstring_parser.common.Docstring object at 0x105bf1390> is None

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_returns_3_test_edge_case_none.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_returns_3_test_edge_case_none.py::test_returns
============================== 1 failed in 0.03s ===============================
"""

from docstring_parser.tests.test_google import parse

def test_returns() -> None:
    """Test parsing returns."""
    # Test for no return section
    docstring = parse("Short description")
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test for single return with colon in description
    docstring = parse("Short description\nReturns:\ndescription")
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"

    # Test for single return with colon in description and additional text
    docstring = parse("Short description\nReturns:\ndescription with: a colon!")
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description with: a colon!"

    # Test for single return type specified
    docstring = parse("Short description\nReturns:\tint: description")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"

    # Test for multiple returns (not supported by Google-style)
    docstring = parse("Short description\nReturns:\tOptional[Mapping[str, List[int]]]: A description: with a colon")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "Optional[Mapping[str, List[int]]]"
    assert docstring.returns.description == "A description: with a colon"

    # Test for yields (not supported by Google-style)
    docstring = parse("Short description\nYields:\tint: description")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"

    # Test for multiple returns with detailed text
    docstring = parse("Short description\nReturns:\tint: description\nwith much text\n\neven some spacing")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == (
        "description\nwith much text\n\neven some spacing"
    )

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_returns_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_returns _________________________________

    def test_returns() -> None:
        """Test parsing returns."""
        # Test for no return section
        docstring = parse("Short description")
        assert docstring.returns is None
        assert docstring.many_returns is not None
        assert len(docstring.many_returns) == 0
    
        # Test for single return with colon in description
        docstring = parse("Short description\nReturns:\ndescription")
        assert docstring.returns is not None
        assert docstring.returns.type_name is None
>       assert docstring.returns.description == "description"
E       AssertionError: assert '' == 'description'
E         
E         - description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_returns_0_test_valid_inputs.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_returns_0_test_valid_inputs.py::test_returns
============================== 1 failed in 0.03s ===============================
"""
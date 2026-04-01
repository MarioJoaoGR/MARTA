
import pytest
from docstring_parser.tests.test_rest import parse

def test_valid_case_single_return_no_type():
    """Test parsing a single return value without type specification in ReST-style docstring."""
    # Test case with no returns specified
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case with return specified without type
    docstring = parse(
        """
        Short description
        :returns: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]

    # Test case with return specified and type hinted without description
    docstring = parse(
        """
        Short description
        :returns int:
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description is None
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_0_test_valid_case_single_return_no_type.py F [100%]

=================================== FAILURES ===================================
____________________ test_valid_case_single_return_no_type _____________________

    def test_valid_case_single_return_no_type():
        """Test parsing a single return value without type specification in ReST-style docstring."""
        # Test case with no returns specified
        docstring = parse(
            """
            Short description
            """
        )
        assert docstring.returns is None
        assert docstring.many_returns is not None
        assert len(docstring.many_returns) == 0
    
        # Test case with return specified without type
        docstring = parse(
            """
            Short description
            :returns: description
            """
        )
        assert docstring.returns is not None
        assert docstring.returns.type_name is None
        assert docstring.returns.description == "description"
        assert not docstring.returns.is_generator
        assert docstring.many_returns == [docstring.returns]
    
        # Test case with return specified and type hinted without description
        docstring = parse(
            """
            Short description
            :returns int:
            """
        )
        assert docstring.returns is not None
        assert docstring.returns.type_name == "int"
>       assert docstring.returns.description is None
E       AssertionError: assert '' is None
E        +  where '' = <docstring_parser.common.DocstringReturns object at 0x10627d8d0>.description
E        +    where <docstring_parser.common.DocstringReturns object at 0x10627d8d0> = <docstring_parser.common.Docstring object at 0x10627d8a0>.returns

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_0_test_valid_case_single_return_no_type.py:39: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_0_test_valid_case_single_return_no_type.py::test_valid_case_single_return_no_type
============================== 1 failed in 0.04s ===============================
"""

import pytest
from docstring_parser.tests.test_rest import parse

def test_valid_input_happy_path():
    """Test standard input with valid ReST-style docstring containing yield statements."""
    
    # Test case 1: No yield statement
    docstring = parse("Short description")
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0
    
    # Test case 2: Yield statement without type specification
    docstring = parse("Short description :yields: description")
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns
    
    # Test case 3: Yield statement with type specification
    docstring = parse("Short description :yields int: description")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_yields_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        """Test standard input with valid ReST-style docstring containing yield statements."""
    
        # Test case 1: No yield statement
        docstring = parse("Short description")
        assert docstring.returns is None
        assert docstring.many_returns is not None
        assert len(docstring.many_returns) == 0
    
        # Test case 2: Yield statement without type specification
        docstring = parse("Short description :yields: description")
>       assert docstring.returns is not None
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x10208bb50>.returns

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_yields_0_test_valid_input_happy_path.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_yields_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.03s ===============================
"""
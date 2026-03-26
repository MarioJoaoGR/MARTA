
# Module: docstring_parser.tests.test_epydoc
# Import the function from its module
from docstring_parser.tests.test_epydoc import test_yields

def test_yields():
    # Test case 1: No yield information in docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test case 2: Yield information present but no type specified
    docstring = parse(
        """
        Short description
        @yield: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator

    # Test case 3: Yield information present with type specified
    docstring = parse(
        """
        Short description
        @yield: description
        @ytype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_yields_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_0.py:6:0: E0102: function already defined line 4 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_0.py:8:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_0.py:16:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_0.py:28:16: E0602: Undefined variable 'parse' (undefined-variable)

"""
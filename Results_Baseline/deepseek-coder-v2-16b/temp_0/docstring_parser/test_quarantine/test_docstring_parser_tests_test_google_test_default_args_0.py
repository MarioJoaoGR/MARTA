
# Module: docstring_parser.tests.test_google
import pytest
from googleparser import parse

def test_default_args():
    """Test parsing default arguments."""
    docstring = parse(
        """A sample function

Args:
    arg1 (int): The firsty arg
    arg2 (str): The second arg
    arg3 (float, optional): The third arg. Defaults to 1.0.
    arg4 (Optional[Dict[str, Any]], optional): The last arg. Defaults to None.
    arg5 (str, optional): The fifth arg. Defaults to DEFAULT_ARG5."""
    )
    
    # Check that the docstring is not None and has the correct number of parameters
    assert docstring is not None
    assert len(docstring.params) == 5

    # Check individual parameter details
    arg3 = docstring.params[2]
    assert arg3.arg_name == "arg3"
    assert arg3.is_optional
    assert arg3.type_name == "float"
    assert arg3.default == "1.0"
    assert arg3.description == "The third arg. Defaults to 1.0."

    arg4 = docstring.params[3]
    assert arg4.arg_name == "arg4"
    assert arg4.is_optional
    assert arg4.type_name == "Optional[Dict[str, Any]]"
    assert arg4.default == "None"
    assert arg4.description == "The last arg. Defaults to None."

    arg5 = docstring.params[4]
    assert arg5.arg_name == "arg5"
    assert arg5.is_optional
    assert arg5.type_name == "str"
    assert arg5.default == "DEFAULT_ARG5"
    assert arg5.description == "The fifth arg. Defaults to DEFAULT_ARG5."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_default_args_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_default_args_0.py:4:0: E0401: Unable to import 'googleparser' (import-error)

"""
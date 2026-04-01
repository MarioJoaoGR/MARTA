
import pytest
from googleparser import parse

def test_default_args() -> None:
    """Test parsing default arguments."""
    docstring = parse(
        """A sample function

A function the demonstrates docstrings

Args:
    arg1 (int): The firsty arg
    arg2 (str): The second arg
    arg3 (float, optional): The third arg. Defaults to 1.0.
    arg4 (Optional[Dict[str, Any]], optional): The last arg. Defaults to None.
    arg5 (str, optional): The fifth arg. Defaults to DEFAULT_ARG5.

Returns:
    Mapping[str, Any]: The args packed in a mapping
"""
    )
    assert docstring is not None
    assert len(docstring.params) == 5

    arg4 = docstring.params[3]
    assert arg4.arg_name == "arg4"
    assert arg4.is_optional
    assert arg4.type_name == "Optional[Dict[str, Any]]"
    assert arg4.default == "None"
    assert arg4.description == "The last arg. Defaults to None."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_default_args_3_test_valid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_default_args_3_test_valid_inputs.py:3:0: E0401: Unable to import 'googleparser' (import-error)


"""

import pytest
from docstring_parser.common import Parameter  # Importing from the correct module

def test_invalid_inputs():
    with pytest.raises(TypeError):
        param = DocstringParam(
            args=["param1", "param2"],
            description="First and second parameters",
            arg_name="example_arg",
            type_name="int",
            is_optional=False,
            default="None"
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_DocstringParam___init___2_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringParam___init___2_test_invalid_inputs.py:3:0: E0611: No name 'Parameter' in module 'docstring_parser.common' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringParam___init___2_test_invalid_inputs.py:7:16: E0602: Undefined variable 'DocstringParam' (undefined-variable)

"""
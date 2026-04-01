
import pytest
from docstring_parser.google import process_one
from docstring_parser.structures import DocstringParam, DocstringReturns, DocstringRaises

def test_valid_input_return():
    param_obj = DocstringParam(arg_name="param1", type_name="int", description="This is a parameter.", is_optional=False)
    process_one(param_obj)
    
    assert len(parts) == 1
    assert parts[0] == "param1 (int):"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_process_one_0_test_valid_input_return
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_return.py:3:0: E0611: No name 'process_one' in module 'docstring_parser.google' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_return.py:4:0: E0401: Unable to import 'docstring_parser.structures' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_return.py:4:0: E0611: No name 'structures' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_return.py:10:15: E0602: Undefined variable 'parts' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_return.py:11:11: E0602: Undefined variable 'parts' (undefined-variable)


"""
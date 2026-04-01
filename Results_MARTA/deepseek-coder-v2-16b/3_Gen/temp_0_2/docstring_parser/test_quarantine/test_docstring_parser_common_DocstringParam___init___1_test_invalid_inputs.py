
import pytest
from docstring_parser.common import DocstringParam

def test_invalid_inputs():
    # Test cases for invalid inputs
    invalid_cases = [
        (None, "description", "argName", "int", True, "default_value"),  # args is None
        ([], "description", "argName", "int", True, "default_value"),   # args is an empty list
        ("args", None, "argName", "int", True, "default_value"),         # description is None
        ("args", "", "argName", "int", True, "default_value"),           # description is an empty string
        ("args", "description", None, "int", True, "default_value"),     # arg_name is None
        ("args", "description", "", "int", True, "default_value"),       # arg_name is an empty string
        ("args", "description", "argName", None, True, "default_value"), # type_name is None
        ("args", "description", "argName", "", True, "default_value"),   # type_name is an empty string
        ("args", "description", "argName", "int", None, "default_value"),# is_optional is None
        ("args", "description", "argName", "int", True, None),           # default is None
    ]
    
    for case in invalid_cases:
        with pytest.raises(TypeError):
            DocstringParam(*case)

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

docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringParam___init___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test cases for invalid inputs
        invalid_cases = [
            (None, "description", "argName", "int", True, "default_value"),  # args is None
            ([], "description", "argName", "int", True, "default_value"),   # args is an empty list
            ("args", None, "argName", "int", True, "default_value"),         # description is None
            ("args", "", "argName", "int", True, "default_value"),           # description is an empty string
            ("args", "description", None, "int", True, "default_value"),     # arg_name is None
            ("args", "description", "", "int", True, "default_value"),       # arg_name is an empty string
            ("args", "description", "argName", None, True, "default_value"), # type_name is None
            ("args", "description", "argName", "", True, "default_value"),   # type_name is an empty string
            ("args", "description", "argName", "int", None, "default_value"),# is_optional is None
            ("args", "description", "argName", "int", True, None),           # default is None
        ]
    
        for case in invalid_cases:
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringParam___init___1_test_invalid_inputs.py:21: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringParam___init___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""

import pytest
from docstring_parser.common import Docstring

def test_invalid_input():
    # Test that an invalid input raises a TypeError
    with pytest.raises(TypeError):
        # Passing an incorrect type of argument to simulate an invalid input
        invalid_style = "invalid_style"
        Docstring(style=invalid_style)

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

docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_params_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test that an invalid input raises a TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_params_1_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_params_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================

"""
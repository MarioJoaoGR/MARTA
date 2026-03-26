
import pytest
import ast
from docstring_parser.attrdoc import ast_get_attribute

def test_none_input():
    # Test when input is None
    with pytest.raises(TypeError):
        ast_get_attribute(None)

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        # Test when input is None
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_none_input.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_none_input.py::test_none_input
============================== 1 failed in 0.03s ===============================

"""
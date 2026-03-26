
import pytest
from dataclasses_json.stringcase import pascalcase

def test_pascalcase_valid_input():
    assert pascalcase("PYTHON programming") == "PythonProgramming"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_valid_input_PYTHON_programming.py F [100%]

=================================== FAILURES ===================================
_________________________ test_pascalcase_valid_input __________________________

    def test_pascalcase_valid_input():
>       assert pascalcase("PYTHON programming") == "PythonProgramming"
E       AssertionError: assert 'PYTHONProgramming' == 'PythonProgramming'
E         
E         - PythonProgramming
E         + PYTHONProgramming

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_valid_input_PYTHON_programming.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_valid_input_PYTHON_programming.py::test_pascalcase_valid_input
============================== 1 failed in 0.03s ===============================
"""
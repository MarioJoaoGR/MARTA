
import pytest
from dataclasses_json import stringcase

def test_pascalcase():
    assert stringcase.pascalcase("hello_world") == "HelloWorld"
    assert stringcase.pascalcase("PYTHON programming") == "PythonProgramming"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_pascalcase ________________________________

    def test_pascalcase():
        assert stringcase.pascalcase("hello_world") == "HelloWorld"
>       assert stringcase.pascalcase("PYTHON programming") == "PythonProgramming"
E       AssertionError: assert 'PYTHONProgramming' == 'PythonProgramming'
E         
E         - PythonProgramming
E         + PYTHONProgramming

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_edge_case_none.py::test_pascalcase
============================== 1 failed in 0.03s ===============================
"""

import re
from dataclasses_json.stringcase import camelcase as cc

def test_valid_case_hello_world():
    assert cc("hello_world") == "HelloWorld"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_0_test_valid_case_hello_world.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_case_hello_world __________________________

    def test_valid_case_hello_world():
>       assert cc("hello_world") == "HelloWorld"
E       AssertionError: assert 'helloWorld' == 'HelloWorld'
E         
E         - HelloWorld
E         ? ^
E         + helloWorld
E         ? ^

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_0_test_valid_case_hello_world.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_0_test_valid_case_hello_world.py::test_valid_case_hello_world
============================== 1 failed in 0.04s ===============================

"""

import pytest
from dataclasses_json.stringcase import capitalcase

def test_capitalcase():
    assert capitalcase("hello") == "Hello"
    assert capitalcase("HELLO WORLD") == "Hello world"
    assert capitalcase("") == ""
    assert capitalcase(12345) == "12345"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_capitalcase_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_capitalcase _______________________________

    def test_capitalcase():
        assert capitalcase("hello") == "Hello"
>       assert capitalcase("HELLO WORLD") == "Hello world"
E       AssertionError: assert 'HELLO WORLD' == 'Hello world'
E         
E         - Hello world
E         + HELLO WORLD

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_capitalcase_0_test_edge_case_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_capitalcase_0_test_edge_case_none.py::test_capitalcase
============================== 1 failed in 0.03s ===============================
"""
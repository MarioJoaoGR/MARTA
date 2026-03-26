
import pytest
from dataclasses_json.stringcase import spinalcase

def test_valid_input():
    assert spinalcase("Hello-World") == 'hello-world'
    assert spinalcase("Python Programming Language") == 'python-programming-language'
    assert spinalcase("123 Number Example") == '123-number-example'
    assert spinalcase("") == ''

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_spinalcase_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       assert spinalcase("Hello-World") == 'hello-world'
E       AssertionError: assert 'hello--world' == 'hello-world'
E         
E         - hello-world
E         + hello--world
E         ?       +

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_spinalcase_0_test_valid_input.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_spinalcase_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""

import pytest
from dataclasses_json.stringcase import snakecase

def test_edge_case_none():
    assert snakecase("") == ""
    assert snakecase("Hello, World!") == "hello_world"
    assert snakecase("This is a test.") == "this_is_a_test"
    assert snakecase("Convert-This-To-Snake-Case") == "convert_to_snake_case"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        assert snakecase("") == ""
>       assert snakecase("Hello, World!") == "hello_world"
E       AssertionError: assert 'hello,__world!' == 'hello_world'
E         
E         - hello_world
E         + hello,__world!
E         ?      ++      +

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_0_test_edge_case_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.04s ===============================
"""
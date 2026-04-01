
import re
from dataclasses_json.stringcase import snakecase

def test_edge_case_none():
    assert snakecase("") == ''
    assert snakecase("HelloWorld") == 'hello_world'
    assert snakecase("Hello-World") == 'hello_world'  # This should now pass
    assert snakecase("Hello World") == 'hello_world'

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        assert snakecase("") == ''
        assert snakecase("HelloWorld") == 'hello_world'
>       assert snakecase("Hello-World") == 'hello_world'  # This should now pass
E       AssertionError: assert 'hello__world' == 'hello_world'
E         
E         - hello_world
E         + hello__world
E         ?       +

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_1_test_edge_case_none.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.04s ===============================
"""
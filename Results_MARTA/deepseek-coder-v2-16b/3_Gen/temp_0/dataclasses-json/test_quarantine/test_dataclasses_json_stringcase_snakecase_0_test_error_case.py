
import re
from dataclasses_json.stringcase import snakecase as sc

def test_error_case():
    assert sc("Hello, World!") == 'hello_world'
    assert sc("This is a test.") == 'this_is_a_test'
    assert sc("Convert-This-To-Snake-Case") == 'convert_to_snake_case'
    assert sc("") == ''

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
>       assert sc("Hello, World!") == 'hello_world'
E       AssertionError: assert 'hello,__world!' == 'hello_world'
E         
E         - hello_world
E         + hello,__world!
E         ?      ++      +

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_0_test_error_case.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_snakecase_0_test_error_case.py::test_error_case
============================== 1 failed in 0.03s ===============================
"""
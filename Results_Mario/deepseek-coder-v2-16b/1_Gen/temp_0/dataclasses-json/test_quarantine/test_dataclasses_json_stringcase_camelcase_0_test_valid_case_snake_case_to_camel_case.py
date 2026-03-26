
import re
from dataclasses_json.stringcase import camelcase

def test_valid_case_snake_case_to_camel_case():
    assert camelcase("snake_case_to_camel_case") == "SnakeCaseToCamelCase"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_0_test_valid_case_snake_case_to_camel_case.py F [100%]

=================================== FAILURES ===================================
___________________ test_valid_case_snake_case_to_camel_case ___________________

    def test_valid_case_snake_case_to_camel_case():
>       assert camelcase("snake_case_to_camel_case") == "SnakeCaseToCamelCase"
E       AssertionError: assert 'snakeCaseToCamelCase' == 'SnakeCaseToCamelCase'
E         
E         - SnakeCaseToCamelCase
E         ? ^
E         + snakeCaseToCamelCase
E         ? ^

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_0_test_valid_case_snake_case_to_camel_case.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_0_test_valid_case_snake_case_to_camel_case.py::test_valid_case_snake_case_to_camel_case
============================== 1 failed in 0.03s ===============================

"""
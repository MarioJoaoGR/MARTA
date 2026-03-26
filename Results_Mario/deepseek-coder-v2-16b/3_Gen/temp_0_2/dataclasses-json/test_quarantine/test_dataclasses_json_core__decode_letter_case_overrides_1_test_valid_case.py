
import pytest
from dataclasses_json.core import _decode_letter_case_overrides

def test_valid_case():
    field_names = ['FirstName', 'lastName']
    overrides = {'firstName': {'letter_case': lambda x: x.lower()}, 'lastname': {'letter_case': lambda x: x.lower()}}
    
    result = _decode_letter_case_overrides(field_names, overrides)
    
    assert result == {'firstname': 'FirstName', 'lastname': 'lastName'}

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_1_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        field_names = ['FirstName', 'lastName']
        overrides = {'firstName': {'letter_case': lambda x: x.lower()}, 'lastname': {'letter_case': lambda x: x.lower()}}
    
        result = _decode_letter_case_overrides(field_names, overrides)
    
>       assert result == {'firstname': 'FirstName', 'lastname': 'lastName'}
E       AssertionError: assert {} == {'firstname':...': 'lastName'}
E         
E         Right contains 2 more items:
E         {'firstname': 'FirstName', 'lastname': 'lastName'}
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_1_test_valid_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_1_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================
"""
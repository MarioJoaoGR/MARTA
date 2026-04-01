
import pytest
from dataclasses_json.core import _decode_letter_case_overrides

def test_valid_input():
    field_names = ['FirstName', 'LastName']
    overrides = {
        'FirstName': {'letter_case': lambda x: x.lower()},
        'LastName': {'letter_case': lambda x: x.upper()}
    }
    
    result = _decode_letter_case_overrides(field_names, overrides)
    
    assert result == {'firstname': 'FirstName', 'lastname': 'LastName'}

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        field_names = ['FirstName', 'LastName']
        overrides = {
            'FirstName': {'letter_case': lambda x: x.lower()},
            'LastName': {'letter_case': lambda x: x.upper()}
        }
    
>       result = _decode_letter_case_overrides(field_names, overrides)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0_test_valid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_names = ['FirstName', 'LastName']
overrides = {'FirstName': {'letter_case': <function test_valid_input.<locals>.<lambda> at 0x10270f370>}, 'LastName': {'letter_case': <function test_valid_input.<locals>.<lambda> at 0x10273c430>}}

    def _decode_letter_case_overrides(field_names, overrides):
        """Override letter case of field names for encode/decode"""
        names = {}
        for field_name in field_names:
            field_override = overrides.get(field_name)
            if field_override is not None:
>               letter_case = field_override.letter_case
E               AttributeError: 'dict' object has no attribute 'letter_case'

dataclasses-json/dataclasses_json/core.py:150: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""

import pytest
from dataclasses_json.core import _decode_letter_case_overrides

# Test cases for _decode_letter_case_overrides
def test_decode_letter_case_overrides():
    # Test case 1: No overrides
    field_names = ['name', 'age']
    overrides = {}
    result = _decode_letter_case_overrides(field_names, overrides)
    expected = {'name': 'name', 'age': 'age'}
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_decode_letter_case_overrides _______________________

    def test_decode_letter_case_overrides():
        # Test case 1: No overrides
        field_names = ['name', 'age']
        overrides = {}
        result = _decode_letter_case_overrides(field_names, overrides)
        expected = {'name': 'name', 'age': 'age'}
>       assert result == expected
E       AssertionError: assert {} == {'age': 'age', 'name': 'name'}
E         
E         Right contains 2 more items:
E         {'age': 'age', 'name': 'name'}
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py:12: AssertionError
_______________ test_decode_letter_case_overrides_with_callable ________________

    def test_decode_letter_case_overrides_with_callable():
        # Test case 2: Overrides with callable
        field_names = ['NAME', 'age']
        overrides = {'NAME': {'letter_case': str.lower}}
>       result = _decode_letter_case_overrides(field_names, overrides)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_names = ['NAME', 'age']
overrides = {'NAME': {'letter_case': <method 'lower' of 'str' objects>}}

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py::test_decode_letter_case_overrides
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py::test_decode_letter_case_overrides_with_callable
============================== 2 failed in 0.03s ===============================

"""
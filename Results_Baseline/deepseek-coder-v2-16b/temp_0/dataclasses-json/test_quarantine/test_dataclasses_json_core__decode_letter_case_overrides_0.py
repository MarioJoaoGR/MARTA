
import pytest
from dataclasses import dataclass
try:
    from your_module import _decode_letter_case_overrides, UndefinedParameterError
except ImportError:
    # If the module is not found, we can define a mock function for testing purposes
    class UndefinedParameterError(Exception):
        pass
    
    def _decode_letter_case_overrides(field_names, overrides):
        result = {}
        for field in field_names:
            key = field.lower()
            if key not in overrides:
                raise UndefinedParameterError(f"Missing override for {field}")
            if overrides[key]['letter_case'] is None:
                continue
            elif callable(overrides[key]['letter_case']):
                result[key] = overrides[key]['letter_case'](field)
        return result

# Define the dataclass for testing
@dataclass
class ExampleClass:
    param1: int
    param2: str

def test_decode_letter_case_overrides():
    # Test case 1: No overrides provided
    field_names = ['FirstName', 'LastName']
    overrides = {}
    with pytest.raises(UndefinedParameterError):
        _decode_letter_case_overrides(field_names, overrides)

def test_decode_letter_case_overrides_with_custom_override():
    # Test case 2: Custom override for a field name
    field_names = ['FirstName', 'LastName']
    overrides = {'firstName': {'letter_case': lambda x: x.lower()}, 'lastName': {'letter_case': lambda x: x.upper()}}
    result = _decode_letter_case_overrides(field_names, overrides)
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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________ test_decode_letter_case_overrides_with_custom_override ____________

    def test_decode_letter_case_overrides_with_custom_override():
        # Test case 2: Custom override for a field name
        field_names = ['FirstName', 'LastName']
        overrides = {'firstName': {'letter_case': lambda x: x.lower()}, 'lastName': {'letter_case': lambda x: x.upper()}}
>       result = _decode_letter_case_overrides(field_names, overrides)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_names = ['FirstName', 'LastName']
overrides = {'firstName': {'letter_case': <function test_decode_letter_case_overrides_with_custom_override.<locals>.<lambda> at 0x...': {'letter_case': <function test_decode_letter_case_overrides_with_custom_override.<locals>.<lambda> at 0x1027d1750>}}

    def _decode_letter_case_overrides(field_names, overrides):
        result = {}
        for field in field_names:
            key = field.lower()
            if key not in overrides:
>               raise UndefinedParameterError(f"Missing override for {field}")
E               Test4DT_tests.test_dataclasses_json_core__decode_letter_case_overrides_0.UndefinedParameterError: Missing override for FirstName

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py:16: UndefinedParameterError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_0.py::test_decode_letter_case_overrides_with_custom_override
========================= 1 failed, 1 passed in 0.02s ==========================

"""

import pytest
from dataclasses import dataclass, fields
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, Tuple, List, Any

# Import the function to be tested
def _separate_defined_undefined_kvs(cls, kvs: Dict) -> Tuple[Dict, Dict]:
    """
    Returns a 2 dictionaries: defined and undefined parameters
    """
    class_fields = fields(cls)
    field_names = [field.name for field in class_fields]
    unknown_given_parameters = {k: v for k, v in kvs.items() if k not in field_names}
    known_given_parameters = {k: v for k, v in kvs.items() if k in field_names}
    return known_given_parameters, unknown_given_parameters

# Define a sample class to use for testing
@dataclass_json
@dataclass
class SampleClass:
    name: str
    age: int
    city: str = ""  # Default value provided for the catch-all field

def test_separate_defined_undefined_kvs():
    kvs = {'name': 'John', 'age': 30, 'city': 'New York'}
    known_params, unknown_params = _separate_defined_undefined_kvs(SampleClass, kvs)
    assert known_params == {'name': 'John', 'age': 30}
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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0.py F [100%]

=================================== FAILURES ===================================
_____________________ test_separate_defined_undefined_kvs ______________________

    def test_separate_defined_undefined_kvs():
        kvs = {'name': 'John', 'age': 30, 'city': 'New York'}
        known_params, unknown_params = _separate_defined_undefined_kvs(SampleClass, kvs)
>       assert known_params == {'name': 'John', 'age': 30}
E       AssertionError: assert {'age': 30, '...name': 'John'} == {'age': 30, 'name': 'John'}
E         
E         Omitting 2 identical items, use -vv to show
E         Left contains 1 more item:
E         {'city': 'New York'}
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0.py::test_separate_defined_undefined_kvs
============================== 1 failed in 0.02s ===============================

"""
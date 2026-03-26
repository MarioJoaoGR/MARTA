
from dataclasses_json.undefined import _IgnoreUndefinedParameters
import pytest
from typing import Dict, Any

# Define the class for testing
class TestClass:
    pass  # This is a placeholder for your actual test class definition if needed

def test_handle_from_dict():
    # Create an instance of the class to be tested
    ignore_undefined = _IgnoreUndefinedParameters()
    
    # Define a dictionary with known and unknown parameters
    kvs = {'param1': 1, 'extra_param': 2}
    
    # Call the method under test
    result = ignore_undefined.handle_from_dict(cls=TestClass, kvs=kvs)
    
    # Assert that only known parameters are returned
    assert result == {'param1': 1}

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
____________________________ test_handle_from_dict _____________________________

    def test_handle_from_dict():
        # Create an instance of the class to be tested
        ignore_undefined = _IgnoreUndefinedParameters()
    
        # Define a dictionary with known and unknown parameters
        kvs = {'param1': 1, 'extra_param': 2}
    
        # Call the method under test
>       result = ignore_undefined.handle_from_dict(cls=TestClass, kvs=kvs)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0_test_edge_cases.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/undefined.py:90: in handle_from_dict
    _UndefinedParameterAction._separate_defined_undefined_kvs(
dataclasses-json/dataclasses_json/undefined.py:51: in _separate_defined_undefined_kvs
    class_fields = fields(cls)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

class_or_instance = <class 'Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0_test_edge_cases.TestClass'>

    def fields(class_or_instance):
        """Return a tuple describing the fields of this dataclass.
    
        Accepts a dataclass or an instance of one. Tuple elements are of
        type Field.
        """
    
        # Might it be worth caching this, per class?
        try:
            fields = getattr(class_or_instance, _FIELDS)
        except AttributeError:
>           raise TypeError('must be called with a dataclass type or instance') from None
E           TypeError: must be called with a dataclass type or instance

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/dataclasses.py:1198: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0_test_edge_cases.py::test_handle_from_dict
============================== 1 failed in 0.04s ===============================
"""

import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

@dataclass
class ExampleClass:
    some_field: str
    another_field: int
    undefined_param: Optional[str] = None

def test_valid_inputs():
    example_class = ExampleClass(some_field='value1', another_field=123, undefined_param=None)
    
    # Create a dictionary with undefined parameters
    kvs = {
        'some_field': 'value1',
        'another_field': 123,
        'undefined_param': 'extra_value'
    }
    
    # Call the handle_to_dict function
    result = _CatchAllUndefinedParameters.handle_to_dict(example_class, kvs)
    
    # Assert that the undefined parameter is removed and other parameters are preserved
    assert 'undefined_param' not in result
    assert result == {'some_field': 'value1', 'another_field': 123}

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        example_class = ExampleClass(some_field='value1', another_field=123, undefined_param=None)
    
        # Create a dictionary with undefined parameters
        kvs = {
            'some_field': 'value1',
            'another_field': 123,
            'undefined_param': 'extra_value'
        }
    
        # Call the handle_to_dict function
>       result = _CatchAllUndefinedParameters.handle_to_dict(example_class, kvs)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_inputs.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/undefined.py:201: in handle_to_dict
    _CatchAllUndefinedParameters._get_catch_all_field(obj.__class__)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_inputs.ExampleClass'>

    @staticmethod
    def _get_catch_all_field(cls) -> Field:
        cls_globals = vars(sys.modules[cls.__module__])
        types = get_type_hints(cls, globalns=cls_globals)
        catch_all_fields = list(
            filter(lambda f: types[f.name] == Optional[CatchAllVar], fields(cls)))
        number_of_catch_all_fields = len(catch_all_fields)
        if number_of_catch_all_fields == 0:
>           raise UndefinedParameterError(
E           dataclasses_json.undefined.UndefinedParameterError: No field of type dataclasses_json.CatchAll defined

dataclasses-json/dataclasses_json/undefined.py:256: UndefinedParameterError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.04s ===============================
"""
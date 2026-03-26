
import pytest
from dataclasses_json.undefined import handle_to_dict, _CatchAllUndefinedParameters

@pytest.fixture
def obj():
    class MyClass:
        my_field: utils.CatchAll = None
    return MyClass()

@pytest.fixture
def kvs():
    return {'my_field': {}}

def test_handle_to_dict(obj, kvs):
    catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(obj.__class__)
    undefined_parameters = kvs.pop(catch_all_field.name)
    if isinstance(undefined_parameters, dict):
        kvs.update(undefined_parameters)  # If desired handle letter case here
    assert kvs == {'my_field': {}}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_inputs.py:3:0: E0611: No name 'handle_to_dict' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_inputs.py:8:18: E0602: Undefined variable 'utils' (undefined-variable)


"""

from dataclasses_json.undefined import CatchAllUndefinedParameters as _CatchAllUndefinedParameters

def handle_to_dict(obj, kvs: Dict[Any, Any]) -> Dict[Any, Any]:
    catch_all_field = \
        _CatchAllUndefinedParameters._get_catch_all_field(obj.__class__)
    undefined_parameters = kvs.pop(catch_all_field.name)
    if isinstance(undefined_parameters, dict):
        kvs.update(
            undefined_parameters)  # If desired handle letter case here
    return kvs

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs.py:2:0: E0611: No name 'CatchAllUndefinedParameters' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs.py:4:29: E0602: Undefined variable 'Dict' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs.py:4:34: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs.py:4:39: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs.py:4:48: E0602: Undefined variable 'Dict' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs.py:4:53: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_invalid_inputs.py:4:58: E0602: Undefined variable 'Any' (undefined-variable)


"""

from dataclasses_json.undefined import handle_to_dict as original_handle_to_dict

def test_valid_input():
    class _CatchAllUndefinedParameters:
        """
            This class allows to add a field of type utils.CatchAll which acts as a
            dictionary into which all
            undefined parameters will be written.
            These parameters are not affected by LetterCase.
            If no undefined parameters are given, this dictionary will be empty.
        """
        class _SentinelNoDefault:
            pass
        
        @staticmethod
        def handle_to_dict(obj, kvs: Dict[Any, Any]) -> Dict[Any, Any]:
            catch_all_field = \
                _CatchAllUndefinedParameters._get_catch_all_field(obj.__class__)
            undefined_parameters = kvs.pop(catch_all_field.name)
            if isinstance(undefined_parameters, dict):
                kvs.update(
                    undefined_parameters)  # If desired handle letter case here
            return kvs
    
    class ExampleDataclass:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    
    example = ExampleDataclass(extra_param1="value1", extra_param2="value2")
    input_kvs = {"catch_all": {"extra_param1": "value1", "extra_param2": "value2"}}
    
    result = handle_to_dict(example, input_kvs)
    assert result == {"extra_param1": "value1", "extra_param2": "value2"}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:2:0: E0611: No name 'handle_to_dict' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:17:37: E0602: Undefined variable 'Dict' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:17:42: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:17:47: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:17:56: E0602: Undefined variable 'Dict' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:17:61: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:17:66: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:19:16: E1101: Class '_CatchAllUndefinedParameters' has no '_get_catch_all_field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0_test_valid_input.py:33:13: E0602: Undefined variable 'handle_to_dict' (undefined-variable)

"""
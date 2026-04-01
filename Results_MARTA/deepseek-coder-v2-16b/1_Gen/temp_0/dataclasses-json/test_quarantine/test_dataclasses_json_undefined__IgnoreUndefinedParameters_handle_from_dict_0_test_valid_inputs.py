
import pytest
from dataclasses_json import undefined
from typing import Dict, Any

class _IgnoreUndefinedParameters:
    """
    This class provides a method to handle undefined parameters by separating them into known and unknown categories. When instantiated, it does nothing with the undefined parameters but allows for their separation based on the class fields.
    
    Parameters:
        cls (class): The class object from which to extract field names. This is necessary to determine which parameters are defined within the class.
        kvs (Dict): A dictionary containing key-value pairs where keys are parameter names and values are their corresponding values. These parameters will be checked against the class fields to determine if they are known or unknown.
    
    Returns:
        Dict[str, Any]: A dictionary containing only the known parameters that match the class fields. The undefined parameters are not included in this output.
    
    Example:
        Given a class with fields 'param1' and 'param2', and a dictionary kvs = {'param1': 1, 'extra_param': 2}, calling handle_from_dict(cls=class_object, kvs=kvs) will return {'param1': 1}. The parameter 'extra_param' is unknown to the class and thus not included in the output.
    """
    def handle_from_dict(cls, kvs: Dict) -> Dict[str, Any]:
        known_given_parameters, _ = \
            _UndefinedParameterAction._separate_defined_undefined_kvs(
                cls=cls, kvs=kvs)
        return known_given_parameters

def test_valid_inputs():
    class TestClass:
        param1: int
        param2: int

    kvs = {'param1': 1, 'param2': 2}
    result = _IgnoreUndefinedParameters.handle_from_dict(cls=TestClass, kvs=kvs)
    
    assert result == {'param1': 1, 'param2': 2}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0_test_valid_inputs.py:20:4: E0213: Method 'handle_from_dict' should have "self" as first argument (no-self-argument)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0_test_valid_inputs.py:22:12: E0602: Undefined variable '_UndefinedParameterAction' (undefined-variable)

"""
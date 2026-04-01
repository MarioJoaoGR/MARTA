
from dataclasses import is_dataclass, fields
from typing import Dict, Any, Type
from dataclasses_json.undefined import _UndefinedParameterAction

class _IgnoreUndefinedParameters:
    """
        This action does nothing when it encounters undefined parameters. The undefined parameters can not be retrieved after the class has been created.
        
        Parameters:
            cls (Type[dataclass]): The dataclass type to be instantiated.
            kvs (Dict): A dictionary containing key-value pairs for initializing the dataclass. These parameters may or may not be defined in the class fields.
            
        Returns:
            Dict[str, Any]: A dictionary with known given parameters. Undefined parameters are ignored and not included in this dictionary.
        
        Example:
            Suppose you have a subclass of `_IgnoreUndefinedParameters` with fields 'param1' and 'param2'. You call the `handle_from_dict` method with kvs = {'param1': 1, 'extra_param': 2}.
            This will return ({'param1': 1}, {}) because 'extra_param' is not defined in the class fields.
        
        Notes:
            - The function does not modify or handle undefined parameters; it simply filters out and returns only the known parameters.
            - If no parameters are known (i.e., all provided keys do not match any field names), an empty dictionary is returned.
    """
    def handle_from_dict(cls, kvs: Dict) -> Dict[str, Any]:
        if not is_dataclass(cls):
            raise ValueError("The provided class must be a dataclass.")
        
        known_given_parameters = {}
        for field in fields(cls):
            if field.name in kvs:
                known_given_parameters[field.name] = kvs[field.name]
        
        return known_given_parameters

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_edge_case.py:25:4: E0213: Method 'handle_from_dict' should have "self" as first argument (no-self-argument)


"""

from dataclasses_json import core as your_module

def _encode_json_type(value, default=_ExtendedEncoder().default):
    """
    Encodes a JSON-compatible type (list or dict) recursively.
    
    Parameters:
        value (Union[List, Dict]): The input value to be encoded. It can be either a list or a dictionary.
        default (Callable): A callable that provides the default encoding for non-JSON types. This is typically an instance method of _ExtendedEncoder.
        
    Returns:
        Union[List, Dict]: A JSON-compatible version of the input value, with all nested lists and dictionaries recursively encoded.
    
    Examples:
        >>> from your_module import _encode_json_type  # Assuming this function is in a module named 'your_module'
        >>> example_list = [1, "string", {"key": "value"}]
        >>> encoded_list = _encode_json_type(example_list)
        >>> print(encoded_list)
        [{}, 1, {}]
        
        >>> example_dict = {"key1": "value1", "key2": [1, 2, 3]}
        >>> encoded_dict = _encode_json_type(example_dict)
        >>> print(encoded_dict)
        {'key1': {}, 'key2': [{}, {}, {}]}
        
    Notes:
        This function is designed to handle nested lists and dictionaries, converting them into a JSON-compatible format. It uses recursion to ensure that all levels of the structure are encoded properly. The default parameter allows for customization of how non-JSON types are handled through an encoder class (_ExtendedEncoder).
    
    Intended Purpose:
        Converts a JSON serializable type to its JSON representation.
        
        This function is used within the `_encode_overrides` function to handle custom serialization of dataclass fields based on provided overrides. It takes an argument and attempts to convert it into a format that can be serialized to JSON, applying any necessary transformations or checks as defined by the `overrides`.
        
        Parameters:
            value (Union[dict, list, str, int, float, bool, None]): The Python object to be converted to a JSON serializable type. This includes dictionaries, lists, strings, integers, floats, booleans, and None types.
            
        Returns:
            Union[dict, list, str, int, float, bool, None]: A JSON serializable version of the input value, with any necessary transformations applied as defined by the `overrides`.
            
        Raises:
            TypeError: If the provided value is not one of the supported types for direct conversion to JSON.
    """
    if isinstance(value, your_module.Json.__args__):  # type: ignore
        if isinstance(value, list):
            return [_encode_json_type(i) for i in value]
        elif isinstance(value, dict):
            return {k: _encode_json_type(v) for k, v in value.items()}
        else:
            return value
    return default(value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_json_type_0_test_empty_list
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_empty_list.py:4:37: E0602: Undefined variable '_ExtendedEncoder' (undefined-variable)


"""
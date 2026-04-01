
import json
from dataclasses import is_dataclass, asdict
from typing import Union, List, Dict
from dataclasses_json.core import _ExtendedEncoder

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
    if isinstance(value, list):
        return [_encode_json_type(i) for i in value]
    elif isinstance(value, dict):
        return {k: _encode_json_type(v) for k, v in value.items()}
    elif is_dataclass(value):
        return asdict(value)
    else:
        return default(value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================
"""
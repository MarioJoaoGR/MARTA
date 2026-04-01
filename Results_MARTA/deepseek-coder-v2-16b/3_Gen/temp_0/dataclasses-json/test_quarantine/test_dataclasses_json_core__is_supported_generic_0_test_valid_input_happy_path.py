
from dataclasses_json.core import _is_supported_generic as original_function
import typing

def _is_supported_generic(type_):
    """
    Determines whether a given type is supported by the system for generic decoding. The function checks if the type is not a subclass of `str`, is a collection (according to Python's typing module), or is an optional type, or is a union type, or is an enum, or is a generic dataclass.
    
    Parameters:
        type_ (Type): The type object to be checked for support.
        
    Returns:
        bool: True if the type is supported, False otherwise.
        
    Examples:
        >>> from typing import List, Optional, Union, Enum
        >>> class MyEnum(Enum):
        ...     A = 1
        >>> print(_is_supported_generic(List[int]))  # Output will depend on whether List[int] is supported
        
        >>> print(_is_supported_generic(Optional[int]))  # Output: True if int is optional, False otherwise
        
        >>> class MyGenericDataclass: pass
        >>> print(_is_supported_generic(MyGenericDataclass))  # Output will depend on whether MyGenericDataclass is a generic dataclass
        
    Notes:
        - This function uses several helper functions to perform the checks, including `_issubclass_safe`, `_is_collection`, `_is_optional`, `is_union_type`, and `_is_generic_dataclass`.
        - The `_issubclass_safe` function is used to safely check if a type is a subclass of another class or type.
        - The `_is_collection` function checks if the type is a collection according to Python's typing module.
        - The `_is_optional` function determines if the type is an optional type, which can be either a subclass of `Optional`, have arguments that include `None`, or be the special type `Any`.
        - The `is_union_type` function checks if the type is a union type.
        - The `_is_generic_dataclass` function determines whether the type is a generic dataclass by checking if its origin is a dataclass.
    """
    if type_ is _NO_ARGS:
        return False
    not_str = not _issubclass_safe(type_, str)
    is_enum = _issubclass_safe(type_, typing.Enum)
    is_generic_dataclass = _is_generic_dataclass(type_)
    return (not_str and _is_collection(type_)) or _is_optional(
        type_) or is_union_type(type_) or is_enum or is_generic_dataclass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:34:16: E0602: Undefined variable '_NO_ARGS' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:36:18: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:37:14: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:37:38: E1101: Module 'typing' has no 'Enum' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:38:27: E0602: Undefined variable '_is_generic_dataclass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:39:24: E0602: Undefined variable '_is_collection' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:39:50: E0602: Undefined variable '_is_optional' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:40:18: E0602: Undefined variable 'is_union_type' (undefined-variable)


"""
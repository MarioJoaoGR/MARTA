
from typing import List, Union, Optional, get_origin, get_args
from dataclasses_json.core import _NO_ARGS

def _is_supported_generic(type_):
    """
    Determines whether the given type is supported as a generic type, considering it's not a string, a collection type, an optional type, or a union type from the `typing` module. This function uses helper functions to check if the type is not a subclass of `str`, if it's a collection type, and if it behaves like an optional type or a union type.

    Parameters:
        type_ (type): The type object to be checked for support as a generic type.

    Returns:
        bool: True if the type is supported as a generic type, False otherwise.

    Examples:
        >>> from typing import List, Union, Optional
        >>> class MyType: pass
        >>> print(_is_supported_generic(List[int]))  # Output will be True
        
        >>> print(_is_supported_generic(str))  # Output will be False
        
        >>> print(_is_supported_generic(Optional[MyType]))  # Output will be True if MyType is not a subclass of str and behaves like an optional type
        
    Notes:
        - This function checks if the provided type is not a subclass of `str`.
        - It then checks if the type is a collection type using `_is_collection`.
        - If neither condition is met, it further checks if the type represents an optional type with `_is_optional` or if it's a union type from the `typing` module.
    """
    if type_ is _NO_ARGS:
        return False
    not_str = not _issubclass_safe(type_, str)
    is_enum = _issubclass_safe(type_, Enum)
    is_generic_dataclass = _is_generic_dataclass(type_)
    return (not_str and _is_collection(type_)) or _is_optional(
        type_) or is_union_type(type_) or is_enum or is_generic_dataclass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2.py:31:18: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2.py:32:14: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2.py:32:38: E0602: Undefined variable 'Enum' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2.py:33:27: E0602: Undefined variable '_is_generic_dataclass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2.py:34:24: E0602: Undefined variable '_is_collection' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2.py:34:50: E0602: Undefined variable '_is_optional' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_1_test_valid_case_2.py:35:18: E0602: Undefined variable 'is_union_type' (undefined-variable)


"""
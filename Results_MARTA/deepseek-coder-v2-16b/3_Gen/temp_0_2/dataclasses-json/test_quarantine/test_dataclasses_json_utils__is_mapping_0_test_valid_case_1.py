
from collections import Mapping
from dataclasses_json.utils import _get_type_origin, _issubclass_safe

def _is_mapping(type_):
    """
    Determines if a given type is a mapping, such as dict, defaultdict, etc. This function uses the origin of the provided type to check against the Mapping class from the typing module.

    Parameters:
        type_ (Type): The type object to be checked for being a mapping.

    Returns:
        bool: True if `type_` is a mapping, False otherwise.

    Examples:
        >>> from collections import defaultdict
        >>> class MyDict(dict): pass
        >>> _is_mapping(MyDict)
        True
        
        >>> class MyList(list): pass
        >>> _is_mapping(MyList)
        False
        
        >>> _is_mapping(dict)
        True
        
    Notes:
        - This function relies on the `_get_type_origin` function to determine the origin of the provided type.
        - It then checks if this origin is a subclass of the Mapping class from the typing module using the `_issubclass_safe` function.
    
    This function is intended to check whether a given type is a mapping type, supporting standard Python types like `dict`, `OrderedDict`, `defaultdict`, and others, by checking against the abstract base class for mappings from the `collections` module.

    Parameters:
        type_ (Type): The type to be checked.

    Returns:
        bool: True if the type is a mapping, False otherwise.
    """
    return _issubclass_safe(_get_type_origin(type_), Mapping)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_0_test_valid_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_1.py:2:0: E0611: No name 'Mapping' in module 'collections' (no-name-in-module)


"""
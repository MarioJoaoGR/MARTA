
from dataclasses_json.utils import _get_type_origin, _issubclass_safe
from collections import Counter

def _is_counter(type_):
    """
    Checks if a given type is a subclass of `collections.Counter`. This function uses helper functions `_get_type_origin` to retrieve the origin of the provided type and `_issubclass_safe` to safely check for subclassing relationships.
    
    Parameters:
        type_ (Type): The type object to be checked against the Counter class.
        
    Returns:
        bool: True if `type_` is a subclass of `collections.Counter`, False otherwise.
        
    Examples:
        >>> from typing import List, Union
        >>> my_list = List[int]
        >>> print(_is_counter(my_list))  # Output will depend on whether the type is a subclass of Counter
        
        >>> mixed_types = Union[int, str]
        >>> print(_is_counter(mixed_types))  # Output will depend on whether the type is a subclass of Counter
    
    Notes:
        - This function relies on `_get_type_origin` to determine the origin of the provided type. If the origin is not determinable or does not match `collections.Counter`, it returns False.
        - It uses `_issubclass_safe` to check if the type is a subclass of `collections.Counter`. This method ensures compatibility with different Python versions and class types.
    """
    return _issubclass_safe(_get_type_origin(type_), Counter)

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
============================ no tests ran in 0.02s =============================
"""
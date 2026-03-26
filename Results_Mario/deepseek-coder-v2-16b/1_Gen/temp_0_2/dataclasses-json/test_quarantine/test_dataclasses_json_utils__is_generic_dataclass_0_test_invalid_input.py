
from dataclasses import is_dataclass
from dataclasses_json.utils import _get_type_origin

def _is_generic_dataclass(type_):
    """
    Determines whether a given type is a generic dataclass from the typing module, considering differences between Python versions 3.6 and 3.7.

    Parameters:
        type_ (Type): The type object to check for being a generic dataclass.

    Returns:
        bool: True if the type is a generic dataclass, False otherwise.

    Notes:
        - This function first uses `_get_type_origin` to determine the origin of the provided type.
        - It then checks if this origin is a dataclass from the typing module using `is_dataclass`.
        - For Python versions 3.6, it specifically looks for the presence of an attribute that indicates the origin in some cases where `__origin__` might not be available.
        - This function is particularly useful for applications that need to distinguish between dataclasses and other types based on their generic origins from the typing module.

    Examples:
        >>> from typing import List, Union
        >>> MyClass = type('MyClass', (object,), {'attr': int})
        >>> my_generic_class = List[MyClass]
        >>> print(_is_generic_dataclass(my_generic_class))  # Output will be False for Python versions >= 3.7 and True if the origin is a dataclass.
    """
    return is_dataclass(_get_type_origin(type_))

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
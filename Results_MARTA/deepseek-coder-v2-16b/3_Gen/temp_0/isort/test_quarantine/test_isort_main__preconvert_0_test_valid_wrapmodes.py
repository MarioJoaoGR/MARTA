
from typing import Any
from pathlib import Path
from enum import Enum

def _preconvert(item: Any) -> str | list[Any]:
    """Preconverts objects from native types into JSONifyiable types"""
    if isinstance(item, (set, frozenset)):
        return list(item)
    if isinstance(item, WrapModes):
        return str(item.name)
    if isinstance(item, Path):
        return str(item)
    if callable(item) and hasattr(item, "__name__"):
        return str(item.__name__)
    raise TypeError(f"Unserializable object {item} of type {type(item)}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main__preconvert_0_test_valid_wrapmodes
isort/Test4DT_tests/test_isort_main__preconvert_0_test_valid_wrapmodes.py:10:24: E0602: Undefined variable 'WrapModes' (undefined-variable)


"""
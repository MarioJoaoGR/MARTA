
import pytest
from dataclasses_json.core import _is_supported_generic, _NO_ARGS
from typing import List, Optional, Union, Type, Any, get_origin, get_args
from enum import Enum

def _issubclass_safe(cls: Type, base: Type) -> bool:
    return issubclass(cls, base) if cls else False

def _is_collection(type_: Type) -> bool:
    return get_origin(type_) in (list, set, frozenset, tuple, dict, Any) and not isinstance(get_args(type_)[0], str)

def _is_optional(type_: Type) -> bool:
    if type_ is None:
        return False
    origin = get_origin(type_)
    args = get_args(type_)
    return (origin is Union and len(args) == 2 and any(arg is type(None) for arg in args)) or \
           (origin is Optional and len(args) == 1 and args[0] is type(None))

def is_union_type(type_: Type) -> bool:
    origin = get_origin(type_)
    return origin is Union and len(get_args(type_)) > 1

def _is_generic_dataclass(type_: Type) -> bool:
    from dataclasses import is_dataclass
    return is_dataclass(type_) and get_origin(type_) is not None

@pytest.mark.parametrize("type_, expected", [
    (List[int], True),
    (Optional[int], True),
    (Union[int, str], True),
    (Enum, False),  # Assuming Enum should be checked separately or imported correctly
    (Any, True)  # Any is a special type that can represent any other type
])
def test_is_supported_generic(type_, expected):
    assert _is_supported_generic(type_) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py . [ 20%]
..F.                                                                     [100%]

=================================== FAILURES ===================================
____________________ test_is_supported_generic[Enum-False] _____________________

type_ = <enum 'Enum'>, expected = False

    @pytest.mark.parametrize("type_, expected", [
        (List[int], True),
        (Optional[int], True),
        (Union[int, str], True),
        (Enum, False),  # Assuming Enum should be checked separately or imported correctly
        (Any, True)  # Any is a special type that can represent any other type
    ])
    def test_is_supported_generic(type_, expected):
>       assert _is_supported_generic(type_) == expected
E       AssertionError: assert True == False
E        +  where True = _is_supported_generic(<enum 'Enum'>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py:37: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_input_happy_path.py::test_is_supported_generic[Enum-False]
========================= 1 failed, 4 passed in 0.03s ==========================

"""
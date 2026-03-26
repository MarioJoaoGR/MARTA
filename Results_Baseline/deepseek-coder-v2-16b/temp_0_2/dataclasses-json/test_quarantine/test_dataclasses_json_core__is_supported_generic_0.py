
# Module: dataclasses_json.core
# test_core.py
from dataclasses_json.core import _is_supported_generic, _NO_ARGS
import typing
from typing import List, Optional, Union, Enum  # Added 'Enum' from 'typing' module
import enum  # Importing the built-in 'enum' module directly
from dataclasses import dataclass

def test_list_int():
    assert _is_supported_generic(List[int]) == True

def test_optional_int():
    assert _is_supported_generic(Optional[int]) == True

def test_union_type():
    class MyUnionType(Union[int, str]): pass
    assert _is_supported_generic(MyUnionType) == True

def test_enum_type():
    class MyEnum(enum.Enum): pass  # Corrected the enum type usage
    assert _is_supported_generic(MyEnum) == True

def test_generic_dataclass():
    @dataclass
    class MyGenericDataClass: pass
    assert _is_supported_generic(MyGenericDataClass) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0.py:6:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)

"""
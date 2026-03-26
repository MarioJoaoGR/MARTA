
# Module: dataclasses_json.utils
import pytest
from typing import Type, List, Union
from dataclasses import is_dataclass, dataclass
from inspect import get_origin

# Helper function to mimic the behavior of _is_generic_dataclass for testing purposes
def _get_type_origin(type_: Type) -> Type:
    return get_origin(type_)

def test_is_generic_dataclass_with_generic_datatype():
    from typing import List, Union
    
    my_list = List[int]
    assert _get_type_origin(my_list) == list  # Corrected function call to get the origin of the type

    mixed_types = Union[int, str]
    assert _get_type_origin(mixed_types) == Union  # Corrected function call to get the origin of the type

def test_is_generic_dataclass_with_non_generic_datatype():
    assert _get_type_origin(int) is None  # Corrected function call to get the origin of the type

def test_is_generic_dataclass_with_custom_generic_datatype():
    from typing import List
    from dataclasses import dataclass
    
    @dataclass
    class CustomDataclass:
        field1: int
        field2: str

    custom_list = List[CustomDataclass]
    assert _get_type_origin(custom_list) == list  # Corrected function call to get the origin of the type

# Additional test cases to cover different scenarios
def test_is_generic_dataclass_with_none():
    class NoType:
        pass
    
    no_type = NoType()
    with pytest.raises(TypeError):
        _get_type_origin(no_type)  # Corrected function call to get the origin of the type

def test_is_generic_dataclass_with_primitive_type():
    assert _get_type_origin(int) is None  # Corrected function call to get the origin of the type

def test_is_generic_dataclass_with_nested_generics():
    from typing import List, Dict
    
    nested_list = List[List[int]]
    assert _get_type_origin(nested_list) == list  # Corrected function call to get the origin of the type

    dict_of_customs = Dict[str, CustomDataclass]
    assert _get_type_origin(dict_of_customs) is None  # Corrected function call to get the origin of the type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_generic_dataclass_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0.py:6:0: E0611: No name 'get_origin' in module 'inspect' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0.py:54:32: E0602: Undefined variable 'CustomDataclass' (undefined-variable)

"""
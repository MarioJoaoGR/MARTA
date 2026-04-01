
import pytest
from dataclasses_json.core import _is_supported_generic, _NO_ARGS
from typing import List, Optional, Union, Enum, Any
from dataclasses import dataclass

@dataclass
class MyGenericDataclass: pass

def test_is_supported_generic():
    # Test for a supported generic type (List[int])
    assert _is_supported_generic(List[int]) == True
    
    # Test for an unsupported type (str)
    assert _is_supported_generic(str) == False
    
    # Test for an optional type (Optional[int])
    assert _is_supported_generic(Optional[int]) == True
    
    # Test for a union type (Union[int, str])
    assert _is_supported_generic(Union[int, str]) == True
    
    # Test for an enum type (Enum)
    class MyEnum(Enum):
        A = 1
    assert _is_supported_generic(MyEnum) == True
    
    # Test for a generic dataclass
    assert _is_supported_generic(MyGenericDataclass) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_cases.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)

"""
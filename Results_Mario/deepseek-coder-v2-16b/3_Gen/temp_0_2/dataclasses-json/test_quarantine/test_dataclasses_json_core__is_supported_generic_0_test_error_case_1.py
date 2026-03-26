
import pytest
from dataclasses_json import core
from typing import List, Optional, Union, Enum, type
from enum import Enum as PyEnum
from dataclasses import is_dataclass

# Assuming _NO_ARGS and other helper functions are defined in the core module
# from dataclasses_json.core import _NO_ARGS, _issubclass_safe, _is_collection, _is_optional, _is_union_type, _is_generic_dataclass

def test_is_supported_generic():
    class MyDataClass: pass
    
    assert core._is_supported_generic(List[int]) == True  # List is a collection type, so it should be supported as a generic
    assert core._is_supported_generic(Optional[int]) == True  # Optional is an optional type, so it should be supported as a generic
    assert core._is_supported_generic(Union[int, str]) == True  # Union is a union type, so it should be supported as a generic
    assert core._is_supported_generic(Enum) == False  # Enum is not a generic dataclass, so it should not be supported
    assert core._is_supported_generic(MyDataClass) == False  # A simple class that does not originate from any of the specified types should not be supported

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_error_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_error_case_1.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_error_case_1.py:4:0: E0611: No name 'type' in module 'typing' (no-name-in-module)


"""
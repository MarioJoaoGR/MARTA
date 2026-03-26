
import pytest
from dataclasses import is_dataclass
from typing import Iterable, Optional, Union
from enum import Enum
from collections import Iterable as _Iterable
from dataclasses_json.core import _is_union_type, _issubclass_safe, _is_collection, _is_optional, _is_generic_dataclass

def test_invalid_case_1():
    class MyList(list): pass
    class MyOptional(Optional[int]): pass
    class MyUnion(Union[int, str]): pass
    class Color(Enum): pass
    class MyColorType(Color): pass
    class MyDataClass: pass
    
    assert not _is_supported_generic(MyList)  # True, since it's a collection type.
    assert not _is_supported_generic(MyOptional)  # True, since it's an optional type.
    assert not _is_supported_generic(MyUnion)  # True, since it's a union type.
    assert not _is_supported_generic(MyColorType)  # True, since it's an enum type.
    assert not _is_supported_generic(MyDataClass)  # False, since it's not a generic dataclass.

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1.py:6:0: E0611: No name 'Iterable' in module 'collections' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1.py:7:0: E0611: No name '_is_union_type' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1.py:17:15: E0602: Undefined variable '_is_supported_generic' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1.py:18:15: E0602: Undefined variable '_is_supported_generic' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1.py:19:15: E0602: Undefined variable '_is_supported_generic' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1.py:20:15: E0602: Undefined variable '_is_supported_generic' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_case_1.py:21:15: E0602: Undefined variable '_is_supported_generic' (undefined-variable)


"""
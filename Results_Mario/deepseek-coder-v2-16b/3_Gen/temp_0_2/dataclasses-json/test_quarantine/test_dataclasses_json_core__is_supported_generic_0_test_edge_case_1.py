
from dataclasses import dataclass
from typing import Optional, get_origin, get_args

@dataclass
class MyOptional:
    value: Optional[int] = None

def _is_supported_generic(type_):
    if type_ is _NO_ARGS:
        return False
    not_str = not _issubclass_safe(type_, str)
    is_enum = _issubclass_safe(type_, Enum)
    is_generic_dataclass = _is_generic_dataclass(type_)
    return (not_str and _is_collection(type_)) or _is_optional(
        type_) or is_union_type(type_) or is_enum or is_generic_dataclass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:10:16: E0602: Undefined variable '_NO_ARGS' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:12:18: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:13:14: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:13:38: E0602: Undefined variable 'Enum' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:14:27: E0602: Undefined variable '_is_generic_dataclass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:15:24: E0602: Undefined variable '_is_collection' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:15:50: E0602: Undefined variable '_is_optional' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_case_1.py:16:18: E0602: Undefined variable 'is_union_type' (undefined-variable)


"""

from dataclasses import is_dataclass
from dataclasses_json.utils import _get_type_origin

def test_is_generic_dataclass():
    from typing import List, Union
    
    # Test with a generic dataclass (List[int])
    my_list = List[int]
    assert _is_generic_dataclass(my_list) is False  # Assuming List[int] is not a dataclass by default
    
    # Test with another generic dataclass (Union[int, str])
    mixed_types = Union[int, str]
    assert _is_generic_dataclass(mixed_types) is False  # Assuming Union[int, str] is not a dataclass by default

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case.py:10:11: E0602: Undefined variable '_is_generic_dataclass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case.py:14:11: E0602: Undefined variable '_is_generic_dataclass' (undefined-variable)


"""
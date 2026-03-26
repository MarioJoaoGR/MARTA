
# Module: dataclasses_json.utils
import pytest
from typing import List, Union
import sys

if sys.version_info.minor == 6:
    _NO_TYPE_ORIGIN = None
else:
    _NO_TYPE_ORIGIN = object()

def test__get_type_origin():
    from typing import List, Union, Optional
    
    # Basic Usage with a Generic Type
    my_list = [1, 2, 3]
    type_of_my_list = type(my_list)
    origin = _get_type_origin(List[int])
    assert origin == list, f"Expected origin to be <class 'list'>, but got {origin}"
    
    # Handling a Type with No Origin
    mixed_types = Union[int, str]
    type_of_mixed_types = type(mixed_types)
    origin = _get_type_origin(mixed_types)
    assert origin == typing.Union, f"Expected origin to be typing.Union, but got {origin}"
    
    # Using the Function in a Script
    def example():
        my_list = [1, 2, 3]
        type_of_my_list = type(my_list)
        origin_list = _get_type_origin(List[int])
        assert origin_list == list, f"Expected origin of List[int] to be <class 'list'>, but got {origin_list}"
        
        mixed_types = Union[int, str]
        type_of_mixed_types = type(mixed_types)
        origin_union = _get_type_origin(mixed_types)
        assert origin_union == typing.Union, f"Expected origin of Union[int, str] to be typing.Union, but got {origin_union}"
    
    # Handling a Type with No Origin (Custom Example)
    from typing import Optional, List
    
    class MyClass:
        def __init__(self, value: int, name: str = None):
            self.value = value
            self.name = name
    
    my_instance = MyClass(value=10)
    type_of_my_instance = type(my_instance)
    origin = _get_type_origin(Optional[List[MyClass]])
    assert origin == typing.Optional, f"Expected origin to be <class 'typing.Optional'>, but got {origin}"
    
    # Using the Function in a Test Case
    import unittest
    
    class TestGetOriginType(unittest.TestCase):
        def test_get_list_origin(self):
            origin = _get_type_origin(List[int])
            self.assertEqual(origin, list)
        
        def test_get_union_origin(self):
            origin = _get_type_origin(Union[int, str])
            self.assertEqual(origin, typing.Union)
    
    if __name__ == "__main__":
        unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:18:13: E0602: Undefined variable '_get_type_origin' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:24:13: E0602: Undefined variable '_get_type_origin' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:25:21: E0602: Undefined variable 'typing' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:31:22: E0602: Undefined variable '_get_type_origin' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:36:23: E0602: Undefined variable '_get_type_origin' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:37:31: E0602: Undefined variable 'typing' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:49:13: E0602: Undefined variable '_get_type_origin' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:50:21: E0602: Undefined variable 'typing' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:57:21: E0602: Undefined variable '_get_type_origin' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:61:21: E0602: Undefined variable '_get_type_origin' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0.py:62:37: E0602: Undefined variable 'typing' (undefined-variable)

"""
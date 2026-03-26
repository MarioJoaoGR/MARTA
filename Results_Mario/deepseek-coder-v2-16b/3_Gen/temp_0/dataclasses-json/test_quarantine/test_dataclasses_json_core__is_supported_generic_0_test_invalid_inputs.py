
import pytest
from typing import List, Optional, Union, Enum
from dataclasses_json.core import _is_supported_generic

def test_invalid_inputs():
    # Test cases for invalid inputs
    assert not _is_supported_generic(int)  # int is not a supported generic type
    assert not _is_supported_generic(str)  # str is not a supported generic type
    assert not _is_supported_generic(List[int])  # List[int] is a supported generic type
    assert not _is_supported_generic(Optional[int])  # Optional[int] is a supported generic type
    assert not _is_supported_generic(Union[int, str])  # Union[int, str] is a supported generic type
    assert not _is_supported_generic(Enum)  # Enum itself is not a supported generic type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_invalid_inputs.py:3:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)


"""

import pytest
from typing import Tuple, Type, Union, cast
from dataclasses_json.utils import _NO_ARGS, _get_type_args

def test_get_type_arg_param():
    # Test with a generic type having multiple arguments
    result = _get_type_arg_param(Tuple[int, str], 1)
    assert isinstance(result, type) and result == str
    
    # Test with a generic type having only one argument
    result = _get_type_arg_param(Tuple[int, str], 0)
    assert isinstance(result, type) and result == int
    
    # Test with no arguments and the specified index does not exist
    result = _get_type_arg_param(Tuple, 0)
    assert result == _NO_ARGS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_arg_param_0_test_valid_input_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0_test_valid_input_happy_path.py:8:13: E0602: Undefined variable '_get_type_arg_param' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0_test_valid_input_happy_path.py:12:13: E0602: Undefined variable '_get_type_arg_param' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0_test_valid_input_happy_path.py:16:13: E0602: Undefined variable '_get_type_arg_param' (undefined-variable)


"""
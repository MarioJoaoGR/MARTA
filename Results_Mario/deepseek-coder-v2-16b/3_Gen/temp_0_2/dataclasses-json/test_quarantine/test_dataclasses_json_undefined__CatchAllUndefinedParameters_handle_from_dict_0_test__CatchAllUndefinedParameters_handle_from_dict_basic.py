
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

@pytest.mark.parametrize("cls, kvs, expected", [
    (ExampleClass, {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}, {'field1': 1, 'field2': 'hello'}),
])
def test__CatchAllUndefinedParameters_handle_from_dict_basic(cls, kvs, expected):
    known_params = handle_from_dict(cls, kvs)
    assert known_params == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test__CatchAllUndefinedParameters_handle_from_dict_basic
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test__CatchAllUndefinedParameters_handle_from_dict_basic.py:8:5: E0602: Undefined variable 'ExampleClass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test__CatchAllUndefinedParameters_handle_from_dict_basic.py:11:19: E0602: Undefined variable 'handle_from_dict' (undefined-variable)


"""
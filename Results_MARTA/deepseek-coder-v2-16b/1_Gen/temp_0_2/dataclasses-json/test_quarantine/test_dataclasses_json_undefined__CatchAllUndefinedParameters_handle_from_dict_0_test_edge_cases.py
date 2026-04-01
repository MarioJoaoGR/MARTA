
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

@pytest.fixture
def cls():
    @dataclass
    class ExampleClass:
        param1: int = 0
        param2: str = "default"
        _catch_all: Dict[str, Any] = None

    return ExampleClass

def test_handle_from_dict(cls):
    kvs = {'param1': 1, 'extra_param': 2}
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(cls=cls(), kvs=kvs)
    catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(cls=cls())

    with pytest.raises(UndefinedParameterError):
        handle_from_dict(cls, kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_edge_cases.py:19:21: E0602: Undefined variable '_UndefinedParameterAction' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_edge_cases.py:20:22: E0602: Undefined variable '_CatchAllUndefinedParameters' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_edge_cases.py:23:8: E0602: Undefined variable 'handle_from_dict' (undefined-variable)


"""
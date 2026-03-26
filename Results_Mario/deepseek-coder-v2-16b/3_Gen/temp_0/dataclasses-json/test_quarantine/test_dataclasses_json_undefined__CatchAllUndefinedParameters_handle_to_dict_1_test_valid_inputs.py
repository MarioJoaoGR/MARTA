
from dataclasses import dataclass
from typing import Dict, Any
import pytest
from dataclasses_json.undefined import CatchAllUndefinedParameters

@pytest.fixture
def valid_inputs():
    return {
        "key1": "value1",
        "key2": "value2"
    }

def test_handle_to_dict(valid_inputs):
    @dataclass
    class ExampleDataclass:
        key1: str
        key2: str
        catch_all: Dict[Any, Any] = CatchAllUndefinedParameters()

    obj = ExampleDataclass(**valid_inputs)
    kvs = {**valid_inputs}
    
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    
    assert "key1" in result
    assert "key2" in result
    assert "catch_all" not in result
    assert len(result) == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_valid_inputs.py:5:0: E0611: No name 'CatchAllUndefinedParameters' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_1_test_valid_inputs.py:24:13: E0602: Undefined variable '_CatchAllUndefinedParameters' (undefined-variable)


"""
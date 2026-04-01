
import pytest
from dataclasses import dataclass, fields
from typing import Union, Mapping, Collection, Dict, List, Any
import copy
from dataclasses_json.core import is_dataclass, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides
from dataclasses_json.utils import _has_encoder_in_global_config, _get_encoder_in_global_config

@pytest.fixture
def sample_dataclass():
    @dataclass
    class MyDataClass:
        name: str
        age: int
    return MyDataClass(name="John Doe", age=30)

def test_asdict_valid_case(sample_dataclass):
    result = _asdict(sample_dataclass)
    assert isinstance(result, dict)
    assert "name" in result and result["name"] == "John Doe"
    assert "age" in result and result["age"] == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__asdict_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_case.py:7:0: E0611: No name '_has_encoder_in_global_config' in module 'dataclasses_json.utils' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_case.py:7:0: E0611: No name '_get_encoder_in_global_config' in module 'dataclasses_json.utils' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_case.py:18:13: E0602: Undefined variable '_asdict' (undefined-variable)

"""
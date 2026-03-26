
import pytest
from dataclasses import dataclass, fields
from typing import Collection, Mapping, Enum
import copy
from dataclasses_json.core import _asdict, is_dataclass, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides, _has_encoder_in_global_config, _get_encoder_in_global_config

@dataclass
class SimpleDataClass:
    name: str
    age: int

def test_edge_case():
    data = SimpleDataClass(name="John Doe", age=30)
    result = _asdict(data)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert result == {'name': 'John Doe', 'age': 30}, "Dictionary representation is incorrect"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__asdict_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_edge_case.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)


"""
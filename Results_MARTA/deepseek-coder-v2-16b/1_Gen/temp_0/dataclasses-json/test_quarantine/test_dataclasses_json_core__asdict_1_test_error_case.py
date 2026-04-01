
import pytest
from dataclasses import is_dataclass, fields
from typing import Collection, Mapping, Enum
import copy
from dataclasses_json.core import _asdict, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides, _has_encoder_in_global_config, _get_encoder_in_global_config

def test_asdict_with_encoder():
    class CustomType:
        pass
    
    with pytest.raises(TypeError):
        obj = CustomType()
        _asdict(obj)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__asdict_1_test_error_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_1_test_error_case.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)

"""
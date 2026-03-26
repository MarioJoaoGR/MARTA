
import pytest
from dataclasses import dataclass, fields
from typing import Collection, Mapping, Union, Enum
import copy
from dataclasses_json.core import is_dataclass, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides, _has_encoder_in_global_config, _get_encoder_in_global_config

def test_invalid_inputs():
    @dataclass
    class Person:
        name: str
        age: int

    person = Person(name="John", age=30)

    # Test invalid input types
    with pytest.raises(TypeError):
        _asdict(person)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__asdict_1_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_1_test_invalid_inputs.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_1_test_invalid_inputs.py:18:8: E0602: Undefined variable '_asdict' (undefined-variable)


"""
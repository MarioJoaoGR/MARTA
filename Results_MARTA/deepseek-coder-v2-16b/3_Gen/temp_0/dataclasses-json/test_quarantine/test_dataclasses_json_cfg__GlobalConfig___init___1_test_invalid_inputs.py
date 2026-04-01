
from dataclasses import dataclass
from typing import Dict, Union, Optional, Callable, Type
import pytest
from marshmallow import MarshmallowField
from dataclasses_json.cfg import _GlobalConfig

def test_invalid_inputs():
    with pytest.raises(TypeError):
        config = _GlobalConfig()
        assert config is not None  # This line will never be reached due to the TypeError being raised

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg__GlobalConfig___init___1_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___1_test_invalid_inputs.py:5:0: E0611: No name 'MarshmallowField' in module 'marshmallow' (no-name-in-module)


"""
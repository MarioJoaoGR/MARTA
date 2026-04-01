
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Union, Optional, Callable, Type
from marshmallow import MarshmallowField
from dataclasses_json.cfg import _GlobalConfig

@pytest.fixture
def config():
    return _GlobalConfig()

def test_init(config):
    assert isinstance(config.encoders, Dict)
    assert isinstance(config.decoders, Dict)
    assert isinstance(config.mm_fields, Dict)
    assert config.encoders == {}
    assert config.decoders == {}
    assert config.mm_fields == {}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg__GlobalConfig___init___1_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___1_test_edge_cases.py:5:0: E0611: No name 'MarshmallowField' in module 'marshmallow' (no-name-in-module)

"""

from dataclasses import dataclass
from typing import Dict, Union, Optional, Callable
from marshmallow import MarshmallowField
import pytest
from dataclasses_json.cfg import _GlobalConfig

@pytest.fixture
def global_config():
    return _GlobalConfig()

def test_global_config_init(global_config):
    assert isinstance(global_config.encoders, Dict)
    assert isinstance(global_config.decoders, Dict)
    assert isinstance(global_config.mm_fields, Dict)
    assert global_config.encoders == {}
    assert global_config.decoders == {}
    assert global_config.mm_fields == {}

def test_register_encoder(global_config):
    def encoder(data):
        return str(data)
    
    global_config.register_encoder(int, encoder)
    assert isinstance(global_config.encoders[int], Callable)
    assert global_config.encoders[int](42) == "42"

def test_register_decoder(global_config):
    def decoder(data):
        return int(data)
    
    global_config.register_decoder(str, decoder)
    assert isinstance(global_config.decoders[str], Callable)
    assert global_config.decoders[str]("42") == 42

def test_register_mm_field(global_config):
    class CustomField(MarshmallowField):
        pass
    
    global_config.register_mm_field(int, CustomField())
    assert isinstance(global_config.mm_fields[int], CustomField)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg__GlobalConfig___init___0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___0_test_valid_inputs.py:4:0: E0611: No name 'MarshmallowField' in module 'marshmallow' (no-name-in-module)


"""
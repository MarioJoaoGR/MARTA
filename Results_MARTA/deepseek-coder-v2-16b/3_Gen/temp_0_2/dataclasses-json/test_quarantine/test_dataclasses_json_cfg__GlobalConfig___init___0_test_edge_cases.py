
import pytest
from dataclasses import dataclass
from typing import Dict, Union, Optional, Callable, Type
from marshmallow import fields as MarshmallowField
from dataclasses_json.cfg import _GlobalConfig

@pytest.fixture
def global_config():
    return _GlobalConfig()

def test_register_encoder(global_config):
    def encoder(data):
        return str(data)
    
    global_config.register_encoder(int, encoder)
    assert isinstance(global_config.encoders[int], Callable)
    assert callable(global_config.encoders[int])

def test_register_decoder(global_config):
    def decoder(data):
        return int(data)
    
    global_config.register_decoder(str, decoder)
    assert isinstance(global_config.decoders[str], Callable)
    assert callable(global_config.decoders[str])

def test_register_mm_field(global_config):
    class CustomField(MarshmallowField):
        pass
    
    global_config.register_mm_field(int, CustomField())
    assert isinstance(global_config.mm_fields[int], CustomField)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg__GlobalConfig___init___0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___0_test_edge_cases.py:29:4: E0239: Inheriting 'MarshmallowField', which is not a class. (inherit-non-class)


"""
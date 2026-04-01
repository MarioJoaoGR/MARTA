
from dataclasses import dataclass
from typing import Dict, Union, Optional, Callable, Type
import pytest
from marshmallow import fields as MarshmallowField  # Assuming this is how you use marshmallow in your code
from dataclasses_json.cfg import _GlobalConfig  # Adjust the import path according to your project structure

# Mocking MarshmallowField for testing purposes
class MockMarshmallowField(MarshmallowField):
    pass

@pytest.fixture
def global_config():
    return _GlobalConfig()

def test_valid_inputs(global_config):
    # Test register_encoder method
    def encoder(data):
        return str(data)
    
    global_config.register_encoder(dict, encoder)
    assert callable(global_config.encoders[dict])

    # Test register_decoder method
    def decoder(data):
        return int(data)
    
    global_config.register_decoder(int, decoder)
    assert callable(global_config.decoders[int])

    # Test register_mm_field method
    field = MockMarshmallowField()
    global_config.register_mm_field(list, field)
    assert isinstance(global_config.mm_fields[list], MockMarshmallowField)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg__GlobalConfig___init___0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___0_test_valid_inputs.py:9:0: E0239: Inheriting 'MarshmallowField', which is not a class. (inherit-non-class)


"""
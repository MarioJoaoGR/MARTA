
import pytest
from dataclasses import dataclass
from typing import Dict, Union, Optional, Callable, Type
from marshmallow import fields as MarshmallowField  # Assuming this is the correct module for MarshmallowField

# Assuming _GlobalConfig is defined in a module named cfg
from dataclasses_json.cfg import _GlobalConfig

@pytest.fixture
def global_config():
    return _GlobalConfig()

def test_invalid_inputs(global_config):
    # Test that the initial state of encoders, decoders, and mm_fields is an empty dictionary
    assert isinstance(global_config.encoders, Dict)
    assert isinstance(global_config.decoders, Dict)
    assert isinstance(global_config.mm_fields, Dict)
    assert global_config.encoders == {}
    assert global_config.decoders == {}
    assert global_config.mm_fields == {}

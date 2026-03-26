
from dataclasses import dataclass
from typing import Dict, Union, Optional, Callable, Type
import pytest
from marshmallow import fields as MarshmallowField
from dataclasses_json.cfg import _GlobalConfig

@pytest.fixture
def global_config():
    return _GlobalConfig()

def test_valid_inputs(global_config):
    assert isinstance(global_config.encoders, Dict)
    assert isinstance(global_config.decoders, Dict)
    assert isinstance(global_config.mm_fields, Dict)
    assert global_config.encoders == {}
    assert global_config.decoders == {}
    assert global_config.mm_fields == {}

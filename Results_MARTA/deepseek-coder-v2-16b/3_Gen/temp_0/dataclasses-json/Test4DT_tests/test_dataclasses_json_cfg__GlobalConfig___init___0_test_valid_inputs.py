
from dataclasses import dataclass
from typing import Dict, Union, Optional, Callable, Type
from marshmallow import fields as MarshmallowField
import pytest
from dataclasses_json.cfg import _GlobalConfig

@pytest.fixture
def global_config():
    return _GlobalConfig()

def test_valid_inputs(global_config):
    assert isinstance(global_config.encoders, Dict)
    assert isinstance(global_config.decoders, Dict)
    assert isinstance(global_config.mm_fields, Dict)

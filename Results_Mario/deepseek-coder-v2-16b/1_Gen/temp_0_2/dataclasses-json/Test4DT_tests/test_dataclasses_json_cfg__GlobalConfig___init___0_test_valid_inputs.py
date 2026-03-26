
import pytest
from dataclasses_json.cfg import _GlobalConfig

def test_valid_inputs():
    config = _GlobalConfig()
    assert isinstance(config, _GlobalConfig)
    assert hasattr(config, 'encoders') and isinstance(config.encoders, dict)
    assert hasattr(config, 'decoders') and isinstance(config.decoders, dict)
    assert hasattr(config, 'mm_fields') and isinstance(config.mm_fields, dict)

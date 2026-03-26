
import pytest
from dataclasses_json.core import cfg  # Assuming cfg is defined in dataclasses_json.core

# Mocking the global config and its decoders
class MockConfig:
    def __init__(self):
        self.decoders = {}

cfg.global_config = MockConfig()

def test_none_input():
    # Test when type is None
    assert not _has_decoder_in_global_config(None)

def _has_decoder_in_global_config(type_):
    return type_ in cfg.global_config.decoders

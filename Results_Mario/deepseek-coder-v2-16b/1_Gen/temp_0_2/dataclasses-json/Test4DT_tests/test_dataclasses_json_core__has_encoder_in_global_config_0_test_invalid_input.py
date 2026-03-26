
import pytest
from dataclasses_json.core import cfg

# Mocking the global configuration with encoders
class MockConfig:
    def __init__(self):
        self.encoders = {}

cfg.global_config = MockConfig()

def test_invalid_input():
    # Test when type is not in the global configuration
    assert not _has_encoder_in_global_config('non_existent_type')

# Function to be tested
def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

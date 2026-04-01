
import pytest
from dataclasses_json.core import cfg

# Mocking the global configuration with encoders
class MockConfig:
    def __init__(self):
        self.encoders = {}

cfg.global_config = MockConfig()

def test_invalid_encoder_type():
    # Check for an invalid encoder type that does not exist in the global configuration
    assert not _has_encoder_in_global_config('non_existent_type')

# Function to check if a specific encoder type is present in the global configuration
def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

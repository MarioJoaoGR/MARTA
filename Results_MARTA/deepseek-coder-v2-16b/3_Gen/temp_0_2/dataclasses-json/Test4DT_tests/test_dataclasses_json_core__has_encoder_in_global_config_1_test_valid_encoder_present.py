
import pytest
from dataclasses_json import core

# Assuming cfg is a global configuration object with an attribute `encoders` that contains encoder types.
class Config:
    def __init__(self):
        self.encoders = set()

cfg = Config()
cfg.global_config = cfg  # Mocking the global config object

def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

# Test function to check if a valid encoder type is present in the global configuration
@pytest.mark.parametrize("encoder_type, expected", [('linear', True), ('non_existent_type', False)])
def test_valid_encoder_present(encoder_type, expected):
    cfg.global_config.encoders = {'linear'}  # Set the encoders in the global config
    assert _has_encoder_in_global_config(encoder_type) == expected

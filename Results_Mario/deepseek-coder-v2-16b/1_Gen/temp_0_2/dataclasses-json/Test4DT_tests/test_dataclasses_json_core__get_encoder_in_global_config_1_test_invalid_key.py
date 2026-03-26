
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is defined in this module

def _get_encoder_in_global_config(type_):
    return cfg.global_config.encoders[type_]

# Test case for invalid key scenario
def test_invalid_key():
    with pytest.raises(KeyError):
        encoder = _get_encoder_in_global_config('non_existent_type')

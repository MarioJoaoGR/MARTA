
import pytest
from dataclasses_json.core import cfg

def _get_decoder_in_global_config(type_):
    return cfg.global_config.decoders[type_]

# Test case for invalid type retrieval from global configuration
def test_invalid_type():
    with pytest.raises(KeyError):
        decoder = _get_decoder_in_global_config('non_existent_type')

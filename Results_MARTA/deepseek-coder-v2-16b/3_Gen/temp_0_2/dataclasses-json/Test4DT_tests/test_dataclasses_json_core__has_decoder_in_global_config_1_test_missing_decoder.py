
import pytest
from dataclasses_json.core import cfg

@pytest.fixture
def setup_global_config():
    # Mocking the global_config object with a decoders attribute
    cfg.global_config = type('GlobalConfig', (object,), {'decoders': {}})

def test_missing_decoder(setup_global_config):
    from dataclasses_json.core import _has_decoder_in_global_config
    
    # Test case for a missing decoder
    assert not _has_decoder_in_global_config("nonexistent_decoder_type")
    
    # Add a decoder to the global configuration and test again
    cfg.global_config.decoders["some_decoder_type"] = lambda x: x
    assert _has_decoder_in_global_config("some_decoder_type")

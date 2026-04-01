
import pytest
from dataclasses_json.core import cfg

@pytest.fixture(autouse=True)
def setup():
    # Mocking the global configuration with a sample decoder dictionary
    cfg.global_config = type('GlobalConfig', (object,), {'decoders': {}})

# Test case for retrieving a decoder when the input type is 'some_type'
def test_none_input():
    from dataclasses_json.core import _get_decoder_in_global_config
    
    # Assuming 'some_type' does not exist in the global configuration
    with pytest.raises(KeyError):
        decoder = _get_decoder_in_global_config('some_type')

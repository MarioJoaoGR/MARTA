
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is defined in the core module

# Mocking the necessary parts of the global configuration
class MockGlobalConfig:
    def __init__(self):
        self.decoders = {
            'some_type': lambda x: x,  # Example decoder function
        }

def test_invalid_input():
    with pytest.raises(KeyError):
        from dataclasses_json.core import _get_decoder_in_global_config
        
        # Mocking the global configuration to return a mock object
        cfg.global_config = MockGlobalConfig()
        
        # This should raise KeyError because 'invalid_type' is not in the decoders dictionary
        decoder = _get_decoder_in_global_config('invalid_type')


import pytest
from dataclasses_json.core import cfg

def _get_decoder_in_global_config(type_):
    return cfg.global_config.decoders[type_]

def test_invalid_input():
    with pytest.raises(KeyError):
        # Mock the global configuration to not have the specified type in its decoders dictionary
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(cfg.global_config, 'decoders', {})
            _get_decoder_in_global_config('some_type')


import pytest
from dataclasses_json import core

# Assuming cfg is part of some configuration module that needs to be imported
# If 'cfg' is supposed to represent global configuration, it should be mocked or properly defined in a setup function.

def test_missing_key():
    # Mock the behavior of cfg and its global_config.decoders dictionary
    with pytest.raises(KeyError):
        core._get_decoder_in_global_config('non_existent_type')

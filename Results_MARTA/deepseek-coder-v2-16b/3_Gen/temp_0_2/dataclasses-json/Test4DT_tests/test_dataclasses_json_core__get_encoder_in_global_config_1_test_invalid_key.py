
import pytest
from dataclasses_json.core import _get_encoder_in_global_config
from unittest.mock import patch, MagicMock

# Mock the cfg module and its global_config attribute
@patch('dataclasses_json.core.cfg')
def test_invalid_key(_mock_cfg):
    # Create a mock for the encoders dictionary in global_config
    _mock_cfg.global_config.encoders = {}
    
    with pytest.raises(KeyError):
        # Attempt to get an encoder for a non-existent key
        _get_encoder_in_global_config('invalid_type')

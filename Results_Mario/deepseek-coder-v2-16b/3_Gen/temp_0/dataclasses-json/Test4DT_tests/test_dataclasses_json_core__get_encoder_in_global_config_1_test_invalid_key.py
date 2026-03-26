
import pytest
from dataclasses_json.core import _get_encoder_in_global_config
from unittest.mock import patch

# Mocking the cfg module and its global_config with encoders dictionary
@patch('dataclasses_json.core.cfg')
def test_invalid_key(_mock_cfg):
    # Define a mock configuration without the key 'some_type'
    _mock_cfg.global_config.encoders = {'valid_key': 'valid_encoder'}
    
    # Expected behavior: Should raise KeyError since 'some_type' is not in encoders
    with pytest.raises(KeyError):
        _get_encoder_in_global_config('some_type')


import pytest
from dataclasses_json.core import _get_decoder_in_global_config
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def mock_cfg():
    with patch('dataclasses_json.core.cfg') as mock_cfg:
        mock_cfg.global_config = MagicMock()
        mock_cfg.global_config.decoders = {'some_type': 'mock_decoder'}
        yield mock_cfg

def test_valid_input():
    result = _get_decoder_in_global_config('some_type')
    assert result == 'mock_decoder'

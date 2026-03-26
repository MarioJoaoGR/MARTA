
from unittest.mock import patch
import pytest
from dataclasses_json.core import cfg

@pytest.mark.parametrize("type_, expected", [
    ('example_decoder', True),
    ('missing_decoder', False)
])
def test_has_decoder_in_global_config(type_, expected):
    with patch('dataclasses_json.core.cfg.global_config.decoders', {'example_decoder': None}):
        from dataclasses_json.core import _has_decoder_in_global_config
        result = _has_decoder_in_global_config(type_)
        assert result == expected

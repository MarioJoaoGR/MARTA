
import pytest
from dataclasses_json.core import cfg

def _get_encoder_in_global_config(type_):
    return cfg.global_config.encoders[type_]

def test_none_input():
    with pytest.raises(KeyError):
        _get_encoder_in_global_config(None)

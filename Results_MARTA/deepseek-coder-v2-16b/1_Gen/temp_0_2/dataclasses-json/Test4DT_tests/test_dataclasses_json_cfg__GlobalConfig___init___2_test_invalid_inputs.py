
import pytest
from dataclasses_json.cfg import _GlobalConfig

def test_invalid_inputs():
    with pytest.raises(AttributeError):
        config = _GlobalConfig()
        getattr(config, 'non_existent_attribute')  # This will raise AttributeError

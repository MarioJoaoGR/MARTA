
import pytest
from isort.exceptions import UnsupportedSettings

def test_invalid_input():
    invalid_settings = {
        "unsupported_setting": {"value": "some_value", "source": "test"}
    }
    
    with pytest.raises(UnsupportedSettings):
        raise UnsupportedSettings(invalid_settings)


import pytest
from isort.exceptions import UnsupportedSettings

def test_unsupported_settings_single_entry():
    unsupported = {
        "max_line_length": {"value": "200", "source": "config file"}
    }
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(unsupported)
    
    assert excinfo.value.unsupported_settings == unsupported
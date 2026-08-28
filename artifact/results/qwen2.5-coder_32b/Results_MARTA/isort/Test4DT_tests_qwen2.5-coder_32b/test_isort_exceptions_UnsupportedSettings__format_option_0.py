
import pytest
from isort.exceptions import UnsupportedSettings

# Example unsupported settings dictionaries
unsupported_settings_example_1 = {
    "some_setting": {"value": "invalid_value", "source": "config file"},
    "another_setting": {"value": 123, "source": "CLI"}
}

unsupported_settings_example_2 = {
    "max_line_length": {"value": 80, "source": "config file"},
    "line_length": {"value": 79, "source": "CLI"}
}

unsupported_settings_example_3 = {
    "unknown_setting": {"value": True, "source": "runtime"}
}

def test_unsupported_settings_with_multiple():
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(unsupported_settings_example_1)
    
    assert str(excinfo.value).startswith("isort was provided settings that it doesn't support:")

def test_unsupported_settings_with_different_sources():
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(unsupported_settings_example_2)
    
    assert str(excinfo.value).startswith("isort was provided settings that it doesn't support:")

def test_unsupported_settings_with_single_setting():
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(unsupported_settings_example_3)
    
    assert str(excinfo.value).startswith("isort was provided settings that it doesn't support:")

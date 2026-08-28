
# Module: isort.exceptions
import pytest
from isort.exceptions import UnsupportedSettings

# Test cases for the UnsupportedSettings class
def test_basic_usage():
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings({
            'settings_name': {'value': 'some_value', 'source': 'config'}
        })
    assert "isort was provided settings that it doesn't support:" in str(excinfo.value)
    assert "Unsupported setting details" not in str(excinfo.value)  # Assuming this is the expected format

def test_specific_setting():
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings({
            'sort_order': {'value': 'custom', 'source': 'CLI'}
        })
    assert "isort was provided settings that it doesn't support:" in str(excinfo.value)
    assert "sort_order" in str(excinfo.value)
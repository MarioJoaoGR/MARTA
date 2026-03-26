
import pytest

from isort.exceptions import UnsupportedSettings


# Test Case 1: Providing a Single Unsupported Setting
def test_single_unsupported_setting():
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings({'setting1': {'value': 'some_value', 'source': 'config'}})
    
    assert "isort was provided settings that it doesn't support:" in str(exc_info.value)
    assert "setting1" in str(exc_info.value)

import pytest
from isort.exceptions import UnsupportedSettings

def test_invalid_input():
    with pytest.raises(UnsupportedSettings):
        raise UnsupportedSettings({"settings_name": {"value": "some_value", "source": "CLI"}})

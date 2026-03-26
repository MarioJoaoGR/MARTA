
import pytest
from isort.settings import Config

@pytest.mark.parametrize("invalid_config", [
    ("non_existent_file.ini",),  # Non-existent settings file
    ({"profile": "unsupported_profile"},),  # Unsupported profile
    ({"settings_file": "invalid_format.txt"},),  # Invalid format settings file
])
def test_error_case(invalid_config):
    with pytest.raises(TypeError) as excinfo:
        Config(**invalid_config)
    
    assert "argument after ** must be a mapping, not" in str(excinfo.value), f"Expected TypeError related to unsupported settings, but got {str(excinfo.value)}"


import pytest
from isort.exceptions import UnsupportedSettings

def test_invalid_input():
    # Test data with invalid unsupported settings format
    invalid_settings = {
        "setting1": {"value": "some_value", "source": "config"},
        "setting2": {"value": "another_value", "source": "cli"}
    }
    
    # Expected error message based on the provided structure of unsupported settings
    expected_error_message = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- setting1 = some_value  (source: 'config')\n"
        "\t- setting2 = another_value  (source: 'cli')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options.\n"
    )
    
    # Act by attempting to raise the exception with invalid input
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(invalid_settings)
    
    # Assert that the raised exception matches the expected error message
    assert str(exc_info.value) == expected_error_message

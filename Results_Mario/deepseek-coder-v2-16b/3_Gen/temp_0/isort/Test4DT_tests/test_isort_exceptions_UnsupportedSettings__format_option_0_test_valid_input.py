
import pytest

from isort.exceptions import UnsupportedSettings


def test_valid_input():
    # Define valid unsupported settings
    invalid_settings = {
        "setting1": {"value": "some_value", "source": "config"},
        "setting2": {"value": "another_value", "source": "cli"}
    }
    
    # Expected error message format
    expected_error_message = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- setting1 = some_value  (source: 'config')\n"
        "\t- setting2 = another_value  (source: 'cli')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options.\n"
    )
    
    # Test the exception raising with valid unsupported settings
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(invalid_settings)
    
    # Assert that the raised exception message matches the expected error message
    assert str(exc_info.value) == expected_error_message

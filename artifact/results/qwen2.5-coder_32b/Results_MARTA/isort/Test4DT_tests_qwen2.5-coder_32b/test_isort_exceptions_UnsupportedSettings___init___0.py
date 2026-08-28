
import pytest
from isort.exceptions import UnsupportedSettings



def test_valid_case_single_unsupported_setting():
    unsupported_settings = {
        "max_line_length": {"value": "80", "source": "config file"}
    }
    try:
        UnsupportedSettings(unsupported_settings)
    except Exception as e:
        assert isinstance(e, UnsupportedSettings)
        assert "isort was provided settings that it doesn't support:" in str(e)

def test_valid_case_multiple_unsupported_settings():
    unsupported_settings = {
        "line_length": {"value": "79", "source": "CLI"},
        "indent_style": {"value": "tab", "source": "config file"}
    }
    try:
        UnsupportedSettings(unsupported_settings)
    except Exception as e:
        assert isinstance(e, UnsupportedSettings)
        assert "isort was provided settings that it doesn't support:" in str(e)
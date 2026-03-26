
# Importing the necessary module from isort exceptions
from isort.exceptions import FormattingPluginDoesNotExist
import pytest

def test_valid_input():
    # Test that an instance of FormattingPluginDoesNotExist can be created with a valid formatter string
    try:
        formatter = "some_formatter"
        raise FormattingPluginDoesNotExist(formatter)
    except FormattingPluginDoesNotExist as e:
        assert str(e) == f"Specified formatting plugin of {formatter} does not exist. "
        assert e.formatter == formatter

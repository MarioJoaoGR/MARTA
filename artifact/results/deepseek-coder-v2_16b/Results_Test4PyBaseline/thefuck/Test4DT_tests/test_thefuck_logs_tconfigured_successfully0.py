# Module: thefuck.logs
import pytest
from thefuck.logs import configured_successfully, color
import colorama  # Ensure that colorama is properly installed in your environment.

# Fixture to provide a configuration object for testing
@pytest.fixture
def valid_configuration():
    return type('Config', (object,), {'reload': 'source ~/.bashrc'})()

@pytest.fixture
def invalid_configuration():
    return type('Config', (object,), {})()

# Test case to check if the function prints a success message with proper formatting and instructions when given a valid configuration
def test_configured_successfully_with_valid_config(capsys, valid_configuration):
    configured_successfully(valid_configuration)
    captured = capsys.readouterr()
    assert "fuck" in captured.out
    assert "alias configured successfully!" in captured.out
    assert "For applying changes run" in captured.out
    assert "or restart your shell." in captured.out
    assert color(colorama.Style.BRIGHT) in captured.out
    assert color(colorama.Style.RESET_ALL) in captured.out
    assert "source ~/.bashrc" in captured.out

# Test case to check if the function raises an error when given an invalid configuration
def test_configured_successfully_with_invalid_config(capsys, invalid_configuration):
    with pytest.raises(AttributeError):
        configured_successfully(invalid_configuration)

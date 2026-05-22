
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.lexers.common import precise

@pytest.mark.parametrize("precise_enabled, expected", [(True, "CUSTOM_TOKEN"), (False, "DEFAULT_TOKEN")])
def test_happy_path(precise_enabled, expected):
    """
    Test the happy path for the `precise` function where it should return the custom token if 'precise' is enabled.
    """
    # Create a mock lexer object with an option to control 'precise' setting
    lexer = MagicMock()
    lexer.options = {"precise": precise_enabled}
    
    # Define the custom and parent tokens based on the test scenario
    if precise_enabled:
        precise_token = "CUSTOM_TOKEN"
    else:
        precise_token = None
    
    # Call the function with mocked lexer, precise token, and parent token
    result = precise(lexer, precise_token, "DEFAULT_TOKEN")
    
    # Assert that the result matches the expected output based on 'precise' setting
    assert result == expected

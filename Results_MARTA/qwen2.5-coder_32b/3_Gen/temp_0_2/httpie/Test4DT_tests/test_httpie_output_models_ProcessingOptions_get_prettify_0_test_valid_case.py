
import pytest
from unittest.mock import patch
from httpie.output.models import ProcessingOptions, PRETTY_STDOUT_TTY_ONLY, Environment

def test_valid_case():
    with patch('httpie.output.models.Environment') as mock_env:
        # Mock the environment object to return a predefined isatty value
        mock_env.return_value.stdout_isatty = True
        
        options = ProcessingOptions()
        env = Environment(stdout_isatty=True)  # Create an instance of Environment with mocked isatty
        prettify_settings = options.get_prettify(env)
        
        assert isinstance(prettify_settings, list), "Expected a list of strings for prettification settings"
        assert len(prettify_settings) > 0, "Expected non-empty list for prettification settings when stdout is a TTY"


import pytest
from unittest.mock import patch
from httpie.output.models import ProcessingOptions, PRETTY_STDOUT_TTY_ONLY, Environment, PRETTY_MAP

def test_valid_input_happy_path():
    with patch('httpie.output.models.Environment.stdout_isatty', return_value=True):
        options = ProcessingOptions(prettify=PRETTY_STDOUT_TTY_ONLY)
        env = Environment()
        assert options.get_prettify(env) == PRETTY_MAP['all']

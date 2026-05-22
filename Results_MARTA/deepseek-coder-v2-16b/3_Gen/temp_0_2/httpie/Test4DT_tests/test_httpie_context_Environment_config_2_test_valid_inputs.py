
import pytest
from unittest.mock import patch
from httpie.context import Environment

def test_valid_inputs():
    with patch('sys.stdin', new=None), \
         patch('sys.stdout', new=None), \
         patch('sys.stderr', new=None):
        env = Environment()
        assert isinstance(env, Environment)
        assert env.config_dir is not None
        assert env.stdin is not None
        assert env.stdout is not None
        assert env.stderr is not None
        assert env.colors == 256
        assert env.program_name == 'http'
        assert env.show_displays is True

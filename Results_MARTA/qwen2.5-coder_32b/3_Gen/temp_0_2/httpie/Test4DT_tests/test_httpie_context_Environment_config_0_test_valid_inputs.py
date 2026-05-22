
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

def test_valid_inputs():
    with patch('httpie.context.sys.stdin', new_callable=MagicMock):
        env = Environment()
        assert hasattr(env, 'args')
        assert hasattr(env, 'is_windows')
        assert hasattr(env, 'config_dir')
        assert hasattr(env, 'stdin')
        assert hasattr(env, 'stdin_isatty')
        assert hasattr(env, 'stdin_encoding')
        assert hasattr(env, 'stdout')
        assert hasattr(env, 'stdout_isatty')
        assert hasattr(env, 'stdout_encoding')
        assert hasattr(env, 'stderr')
        assert hasattr(env, 'stderr_isatty')
        assert hasattr(env, 'colors')
        assert hasattr(env, 'program_name')
        assert hasattr(env, 'show_displays')
        assert hasattr(env, '_orig_stderr')
        assert hasattr(env, '_devnull')
        assert hasattr(env, 'quiet')
        assert hasattr(env, '_config')

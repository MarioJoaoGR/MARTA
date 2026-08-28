
import pytest
from httpie.context import Environment
import sys
import os
from unittest.mock import patch

def test_default_initialization():
    env = Environment()
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdin')
    assert hasattr(env, 'stdout')
    assert hasattr(env, 'stderr')
    assert hasattr(env, 'colors')
    assert hasattr(env, 'program_name')

def test_custom_configuration():
    with patch.dict('sys.modules', {'colorama': None}):  # Mock colorama to avoid actual terminal handling
        env = Environment(is_windows=False, config_dir='/custom/config/path', program_name='custom_http')
        assert not env.is_windows
        assert env.config_dir == '/custom/config/path'
        assert env.program_name == 'custom_http'


def test_devnull_simulation():
    devnull_mock = open(os.devnull, 'w+')
    env = Environment(devnull=devnull_mock)
    assert isinstance(env._devnull, type(devnull_mock))


import pytest
from httpie.context import Environment
import sys
import io

def test_default_initialization():
    env = Environment()
    assert hasattr(env, 'is_windows'), "Environment should have an attribute is_windows"
    assert isinstance(env.is_windows, bool), "Attribute is_windows should be a boolean"

def test_custom_configuration_with_devnull():
    devnull_mock = io.StringIO()
    env = Environment(devnull=devnull_mock)
    assert env._devnull == devnull_mock, "Environment's _devnull should be the provided mock"


def test_stdout_isatty_default():
    env = Environment()
    assert not env.stdout_isatty, "Default stdout should not be a TTY device"

def test_stderr_isatty_default():
    env = Environment()
    assert not env.stderr_isatty, "Default stderr should not be a TTY device"
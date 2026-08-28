
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
    assert hasattr(env, '_devnull'), "_devnull attribute should exist in the environment"
    assert env._devnull is not None, "The _devnull attribute should be set to the mock file object"

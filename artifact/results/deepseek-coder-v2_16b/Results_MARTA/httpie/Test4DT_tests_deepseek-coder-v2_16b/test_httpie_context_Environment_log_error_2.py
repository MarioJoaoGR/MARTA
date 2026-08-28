
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
    assert hasattr(env, 'devnull'), "Environment should have a devnull attribute"
    assert env.devnull == devnull_mock, "devnull attribute should be the mock object"

def test_custom_configuration_with_config_dir():
    env = Environment(config_dir='/custom/path')
    assert hasattr(env, 'config_dir'), "Environment should have a config_dir attribute"
    assert env.config_dir == '/custom/path', "config_dir attribute should be set to /custom/path"

def test_custom_configuration_with_program_name():
    env = Environment(program_name='myprogram')
    assert hasattr(env, 'program_name'), "Environment should have a program_name attribute"
    assert env.program_name == 'myprogram', "program_name attribute should be set to myprogram"

def test_custom_configuration_with_all_parameters():
    devnull_mock = io.StringIO()
    env = Environment(devnull=devnull_mock, config_dir='/custom/path', program_name='myprogram')
    assert hasattr(env, 'devnull'), "Environment should have a devnull attribute"
    assert env.devnull == devnull_mock, "devnull attribute should be the mock object"
    assert hasattr(env, 'config_dir'), "Environment should have a config_dir attribute"
    assert env.config_dir == '/custom/path', "config_dir attribute should be set to /custom/path"
    assert hasattr(env, 'program_name'), "Environment should have a program_name attribute"
    assert env.program_name == 'myprogram', "program_name attribute should be set to myprogram"

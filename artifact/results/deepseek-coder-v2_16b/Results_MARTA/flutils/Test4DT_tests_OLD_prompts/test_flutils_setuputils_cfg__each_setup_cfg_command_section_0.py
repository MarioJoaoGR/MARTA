
import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section
from unittest.mock import patch

def test_valid_input():
    cfg_parser = ConfigParser()
    cfg_parser['setup.command.build'] = {'command': 'python setup.py build'}
    cfg_parser['setup.command.install'] = {'command': 'python setup.py install'}
    
    expected_output = [('setup.command.build', 'build'), ('setup.command.install', 'install')]
    
    result = list(_each_setup_cfg_command_section(cfg_parser))
    assert result == expected_output

def test_no_sections():
    cfg_parser = ConfigParser()
    
    expected_output = []
    
    result = list(_each_setup_cfg_command_section(cfg_parser))
    assert result == expected_output

@patch('flutils.setuputils.cfg._each_setup_cfg_command_section')
def test_mocked_input(mock_each_setup_cfg_command_section):
    mock_each_setup_cfg_command_section.return_value = [('setup.command.build', 'build'), ('setup.command.install', 'install')]
    
    cfg_parser = ConfigParser()
    cfg_parser['setup.command.build'] = {'command': 'python setup.py build'}
    cfg_parser['setup.command.install'] = {'command': 'python setup.py install'}
    
    result = list(_each_setup_cfg_command_section(cfg_parser))
    assert result == [('setup.command.build', 'build'), ('setup.command.install', 'install')]

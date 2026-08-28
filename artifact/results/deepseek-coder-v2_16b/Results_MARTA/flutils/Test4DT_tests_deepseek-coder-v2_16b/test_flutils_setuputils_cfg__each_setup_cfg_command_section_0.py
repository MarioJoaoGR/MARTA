
import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section
from typing import Generator, Tuple, cast

def test_valid_config_parser():
    cfg_parser = ConfigParser()
    cfg_parser['setup.command.build'] = {'command': 'python setup.py build'}
    cfg_parser['setup.command.install'] = {'command': 'python setup.py install'}
    
    expected_output = [('setup.command.build', 'build'), ('setup.command.install', 'install')]
    result = list(_each_setup_cfg_command_section(cfg_parser))
    
    assert result == expected_output

def test_empty_config_parser():
    cfg_parser = ConfigParser()
    
    expected_output = []
    result = list(_each_setup_cfg_command_section(cfg_parser))
    
    assert result == expected_output

def test_no_sections_in_config_parser():
    cfg_parser = ConfigParser()
    # No sections added to the parser
    
    expected_output = []
    result = list(_each_setup_cfg_command_section(cfg_parser))
    
    assert result == expected_output

# Module: flutils.setuputils.cfg
import pytest
from configparser import ConfigParser
from typing import Generator, Tuple
from flutils.setuputils.cfg import _each_setup_cfg_command_section

# Test data for the function
test_data = [
    (
        {
            'setup.command.build': {'command': 'python setup.py build'},
            'setup.command.install': {'command': 'python setup.py install'}
        },
        [('setup.command.build', 'build'), ('setup.command.install', 'install')]
    ),
    (
        {
            'setup.command.foo': {'command': 'some_command'},
            'setup.command.bar': {'command': 'another_command'}
        },
        [('setup.command.foo', 'foo'), ('setup.command.bar', 'bar')]
    ),
    (
        {},
        []
    )
]

@pytest.mark.parametrize("config_parser, expected", test_data)
def test_each_setup_cfg_command_section(config_parser: dict, expected: list):
    parser = ConfigParser()
    for section, config in config_parser.items():
        parser[section] = config
    
    result = list(_each_setup_cfg_command_section(parser))
    assert result == expected

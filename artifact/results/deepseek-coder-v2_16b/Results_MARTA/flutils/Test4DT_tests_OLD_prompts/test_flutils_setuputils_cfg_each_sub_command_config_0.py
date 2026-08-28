
import os
from configparser import ConfigParser
from typing import Generator, Optional, Union
import pytest
from unittest.mock import patch
from flutils.setuputils.cfg import each_sub_command_config, _get_name

@pytest.fixture(scope="module")
def valid_directory():
    with patch('flutils.setuputils.cfg._prep_setup_dir', return_value='/path/to/myproject'):
        yield '/path/to/myproject'

@pytest.fixture(scope="module")
def none_input():
    with patch('flutils.setuputils.cfg._prep_setup_dir', return_value=os.getcwd()):
        yield None

def test_valid_directory(valid_directory):
    setup_cfg_path = os.path.join(valid_directory, 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, setup_cfg_path)
    assert "The config file, '/path/to/myproject/setup.cfg', is missing the 'metadata' section." in str(excinfo.value)

def test_none_input(none_input):
    with pytest.raises(LookupError) as excinfo:
        for cmd_config in each_sub_command_config():
            pass
    assert "The config file, '/data/results/harness/sandbox/marta/setup.cfg', is missing the 'metadata' section." in str(excinfo.value)

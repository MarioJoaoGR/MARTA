
import os
import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import each_sub_command_config, _get_name, _prep_setup_dir
from typing import Optional, Union, Generator, Dict

# Test for valid input scenario
def test_valid_input():
    mock_setup_dir = 'test_directory'
    mock_parser = ConfigParser()
    mock_parser['DEFAULT'] = {'name': 'TestProject'}
    
    with pytest.raises(LookupError) as excinfo:
        with pytest.MonkeyPatch.context() as mp_mock:
            mp_mock.setattr('flutils.setuputils.cfg._prep_setup_dir', lambda x: mock_setup_dir)
            gen = each_sub_command_config(mock_setup_dir)
            config = next(gen)
    
    assert str(excinfo.value) == "The config file, 'test_directory/setup.cfg', is missing the 'metadata' section."

# Test for None input scenario

# Test for invalid directory scenario
def test_invalid_directory():
    mock_setup_dir = 'non_existent_directory'
    with pytest.raises(FileNotFoundError):
        with pytest.MonkeyPatch.context() as mp_mock:
            mp_mock.setattr('os.path.isfile', lambda x: False)
            gen = each_sub_command_config(mock_setup_dir)
            next(gen)
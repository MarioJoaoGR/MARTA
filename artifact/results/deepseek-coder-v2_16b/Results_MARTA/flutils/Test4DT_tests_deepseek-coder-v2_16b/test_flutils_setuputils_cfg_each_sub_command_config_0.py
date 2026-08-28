
import os
from configparser import ConfigParser
from typing import Generator, Optional, Union, Dict
import pytest
from flutils.setuputils.cfg import each_sub_command_config, _prep_setup_dir, _validate_setup_dir

@pytest.fixture(scope="module")
def valid_path():
    return 'valid_path'


def test_none_input():
    with pytest.raises(FileNotFoundError):
        generator = each_sub_command_config()
        list(generator)
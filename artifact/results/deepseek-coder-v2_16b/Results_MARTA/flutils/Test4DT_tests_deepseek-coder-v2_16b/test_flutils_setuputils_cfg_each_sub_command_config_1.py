
import os
from configparser import ConfigParser
from typing import Generator, Optional, Union
import pytest
from flutils.setuputils.cfg import each_sub_command_config

# Define a simple data class to represent command configurations for testing purposes
class SetupCfgCommandConfig:
    def __init__(self, name: str):
        self.name = name

# Fixture to provide valid project directory
@pytest.fixture
def valid_project_dir():
    return 'tests/fixtures/valid_project'


def test_each_sub_command_config_with_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config('non_existent_directory'))
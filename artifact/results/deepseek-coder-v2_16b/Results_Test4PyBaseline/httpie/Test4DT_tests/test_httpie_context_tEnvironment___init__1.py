
import pytest
from pathlib import Path
import sys
from typing import Optional, IO
from httpie.context import Environment

@pytest.fixture(scope="module")
def default_env():
    return Environment()

@pytest.fixture(scope="module")
def custom_streams_env():
    custom_stdin = open('custom_input.txt', 'r')
    custom_stdout = open('custom_output.txt', 'w')
    custom_stderr = open('custom_error.txt', 'w')
    return Environment(stdin=custom_stdin, stdout=custom_stdout, stderr=custom_stderr)

@pytest.fixture(scope="module")
def config_dir_env():
    config_dir = Path('/custom/config/directory')
    program_name = 'my_program'
    return Environment(config_dir=config_dir, program_name=program_name)

@pytest.fixture(scope="module")
def stdin_encoding_env():
    custom_stdin = open('custom_input.txt', 'r')
    return Environment(stdin=custom_stdin)

@pytest.fixture(scope="module")
def stdout_encoding_env():
    custom_stdout = open('custom_output.txt', 'w')
    return Environment(stdout=custom_stdout)

def test_default_initialization(default_env):
    env = default_env
    assert isinstance(env.is_windows, bool)
    assert isinstance(env.config_dir, Path)
    assert isinstance(env.stdin, Optional[IO])
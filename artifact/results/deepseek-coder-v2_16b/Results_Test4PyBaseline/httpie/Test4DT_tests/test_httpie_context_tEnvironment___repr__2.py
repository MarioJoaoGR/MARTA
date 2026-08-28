
import pytest
from httpie.context import Environment
import sys
from pathlib import Path

@pytest.fixture
def default_env():
    return Environment()

@pytest.fixture
def custom_env():
    stdin = open('custom_input.txt', 'r')
    stdout = open('custom_output.txt', 'w')
    stderr = open('custom_error.txt', 'w')
    return Environment(stdin=stdin, stdout=stdout, stderr=stderr)

@pytest.fixture
def config_env():
    return Environment(config_dir='/custom/config/directory', program_name='my_program')

def test_default_initialization(default_env):
    assert default_env.is_windows == (sys.platform == 'win32')
    assert isinstance(default_env.config_dir, Path)
    assert default_env.stdin == sys.stdin
    assert default_env.stdin_isatty == sys.stdin.isatty()
    assert default_env.stdout == sys.stdout
    assert default_env.stdout_isatty == sys.stdout.isatty()
    assert default_env.stderr == sys.stderr
    assert default_env.stderr_isatty == sys.stderr.isatty()
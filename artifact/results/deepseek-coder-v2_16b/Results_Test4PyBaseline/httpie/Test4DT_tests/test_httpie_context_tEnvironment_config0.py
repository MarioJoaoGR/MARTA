
# Module: httpie.context
# test_environment.py
from pathlib import Path
import sys
from typing import Optional, IO
import pytest
from httpie.context import Environment

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
def custom_config_env():
    return Environment(config_dir='/custom/config/directory', program_name='my_program')

@pytest.fixture
def devnull_env():
    stdin = open('/dev/null', 'r')
    stdout = open('/dev/null', 'w')
    stderr = open('/dev/null', 'w')
    return Environment(stdin=stdin, stdout=stdout, stderr=stderr)

@pytest.fixture
def custom_encoding_env():
    stdin = open('custom_input.txt', 'r', encoding='utf-16')
    stdout = open('custom_output.txt', 'w', encoding='ascii')
    return Environment(stdin=stdin, stdout=stdout)

def test_default_initialization(default_env):
    assert default_env.is_windows == (sys.platform == 'win32')
    assert isinstance(default_env.config_dir, Path)
    assert default_env.stdin == sys.stdin
    assert default_env.stdin_isatty == sys.stdin.isatty()
    assert default_env.stdout == sys.stdout
    assert default_env.stdout_isatty == sys.stdout.isatty()
    assert default_env.stderr == sys.stderr
    assert default_env.stderr_isatty == sys.stderr.isatty()
    assert default_env.colors == 256
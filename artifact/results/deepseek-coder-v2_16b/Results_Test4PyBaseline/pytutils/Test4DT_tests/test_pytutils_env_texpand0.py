# Module: pytutils.env
import pytest
import os
from pytutils.env import expand

# Test expanding a user home directory placeholder
def test_expand_tilde():
    assert expand("~/Documents") == f"{os.path.expanduser('~')}/Documents"

# Test expanding an environment variable placeholder
def test_expand_env_var():
    os.environ['HOME'] = '/home/user'
    assert expand("$HOME/Projects") == "/home/user/Projects"
    del os.environ['HOME']

# Test expanding both placeholders in a string
def test_expand_both():
    os.environ['HOME'] = '/home/user'
    assert expand("$HOME/Downloads") == "/home/user/Downloads"
    del os.environ['HOME']

# Test leaving undefined environment variables unchanged
def test_expand_undefined_env_var():
    assert expand("$UNDEFINED/path") == "$UNDEFINED/path"

# Test expanding an empty string
def test_expand_empty_string():
    assert expand("") == ""

# Test expanding a string without any placeholders
def test_expand_no_placeholders():
    assert expand("C:/Program Files") == "C:/Program Files"

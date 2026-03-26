
import pytest
import os
from pytutils import env

# Test case for expand function with a simple variable expansion
def test_expand_simple_variable():
    assert env.expand("~/Documents") == os.path.expanduser("~/Documents")

# Test case for expand function with an environment variable
def test_expand_environment_variable(monkeypatch):
    monkeypatch.setenv('USER', 'john_doe')
    assert env.expand("$USER/Desktop") == "john_doe/Desktop"

# Test case for expand function with a non-existent environment variable
def test_expand_non_existent_environment_variable(monkeypatch):
    monkeypatch.setenv('NONEXISTENT', 'value')
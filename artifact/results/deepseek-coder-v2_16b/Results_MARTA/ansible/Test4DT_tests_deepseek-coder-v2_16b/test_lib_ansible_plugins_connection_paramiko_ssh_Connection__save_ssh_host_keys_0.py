
import pytest
from lib.ansible.plugins.connection import paramiko_ssh
import os

@pytest.fixture
def setup_conn():
    conn = paramiko_ssh.Connection()
    return conn


def test_invalid_input():
    with pytest.raises(TypeError):
        conn = paramiko_ssh.Connection()  # This should raise a TypeError due to missing arguments
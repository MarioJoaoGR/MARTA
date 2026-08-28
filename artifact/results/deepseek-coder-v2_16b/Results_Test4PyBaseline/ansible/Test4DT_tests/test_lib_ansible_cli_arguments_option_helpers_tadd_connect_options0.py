
import argparse
import pytest
from unittest.mock import patch

# Import the function to be tested
from ansible.cli.arguments.option_helpers import add_connect_options

@pytest.fixture
def parser():
    return argparse.ArgumentParser()

def test_add_connect_options_basic(parser):
    """Test basic usage of add_connect_options"""
    add_connect_options(parser)
    args = parser.parse_args(['--private-key', 'path/to/key', '-u', 'user123', '--connection', 'paramiko'])
    assert hasattr(args, 'private_key_file')
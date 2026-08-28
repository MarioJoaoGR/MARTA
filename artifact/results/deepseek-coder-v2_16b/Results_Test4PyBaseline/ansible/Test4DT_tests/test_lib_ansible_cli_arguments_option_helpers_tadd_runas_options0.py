# Module: ansible.cli.arguments.option_helpers
import argparse
import pytest
from ansible.cli.arguments.option_helpers import add_runas_options

@pytest.fixture
def parser():
    return argparse.ArgumentParser()

def test_add_runas_options_with_become(parser):
    """Test adding the --become option."""
    add_runas_options(parser)
    args = parser.parse_args(['--become'])
    assert args.become is True

def test_add_runas_options_with_become_method(parser):
    """Test adding the --become-method option with a specific method."""
    add_runas_options(parser)
    args = parser.parse_args(['--become-method', 'sudo'])
    assert args.become_method == 'sudo'

def test_add_runas_options_with_become_user(parser):
    """Test adding the --become-user option with a specific user."""
    add_runas_options(parser)
    args = parser.parse_args(['--become-user', 'root'])
    assert args.become_user == 'root'

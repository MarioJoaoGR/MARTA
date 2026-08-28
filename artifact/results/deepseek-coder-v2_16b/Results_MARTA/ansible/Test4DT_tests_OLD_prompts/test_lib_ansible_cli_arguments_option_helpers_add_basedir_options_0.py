
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_basedir_options

# Test scenario 1: Adding the --playbook-dir option to a new ArgumentParser instance
def test_add_basedir_options_new_parser():
    parser = ArgumentParser()
    add_basedir_options(parser)
    args = parser.parse_args(['--playbook-dir', '/custom/path'])
    assert args.basedir == '/custom/path'

# Test scenario 2: Adding the --playbook-dir option to an existing ArgumentParser instance with a custom option
def test_add_basedir_options_existing_parser():
    parser = ArgumentParser()
    parser.add_argument('--custom-option', action='store_true')
    add_basedir_options(parser)
    args = parser.parse_args(['--playbook-dir', '/custom/path', '--custom-option'])
    assert args.basedir == '/custom/path'
    assert args.custom_option is True

# Test scenario 3: Adding the --playbook-dir option to a custom ArgumentParser initialization
def test_add_basedir_options_custom_parser():
    parser = ArgumentParser(description="A tool to manage basedir options")
    add_basedir_options(parser)
    args = parser.parse_args(['--playbook-dir', '/custom/path'])
    assert args.basedir == '/custom/path'

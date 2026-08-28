
import pytest
from ansible.cli.arguments.option_helpers import create_base_parser
import argparse
from unittest.mock import patch

def test_create_base_parser_with_all_parameters():
    prog = "ansible-playbook"
    usage = "Usage: ansible-playbook [options]"
    desc = "Run playbooks"
    epilog = "End of help message."
    
    parser = create_base_parser(prog, usage, desc, epilog)
    assert isinstance(parser, argparse.ArgumentParser), "Expected an ArgumentParser instance"

def test_create_base_parser_without_optional_parameters():
    prog = "ansible-playbook"
    
    parser = create_base_parser(prog)
    assert isinstance(parser, argparse.ArgumentParser), "Expected an ArgumentParser instance"

def test_create_base_parser_with_only_required_parameter():
    prog = "ansible-playbook"
    usage = ""
    desc = None
    epilog = None
    
    parser = create_base_parser(prog, usage, desc, epilog)
    assert isinstance(parser, argparse.ArgumentParser), "Expected an ArgumentParser instance"

def test_create_base_parser_with_custom_usage():
    prog = "ansible-playbook"
    usage = "Usage: ansible-playbook [options]"
    desc = None
    epilog = None
    
    parser = create_base_parser(prog, usage)
    assert isinstance(parser, argparse.ArgumentParser), "Expected an ArgumentParser instance"

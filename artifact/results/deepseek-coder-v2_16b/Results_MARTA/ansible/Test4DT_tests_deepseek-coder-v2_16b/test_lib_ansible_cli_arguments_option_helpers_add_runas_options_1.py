
import pytest
import argparse
from ansible.cli.arguments.option_helpers import add_runas_options, C

def test_add_runas_options():
    parser = argparse.ArgumentParser(description="Script to manage privilege escalation options")
    add_runas_options(parser)
    
    # Test that the --become option is added correctly
    args = parser.parse_args(['--become'])
    assert args.become == True
    
    # Test that the --become-method option is added correctly with default value
    args = parser.parse_args([])
    assert args.become_method == C.DEFAULT_BECOME_METHOD
    
    # Test that the --become-user option is added correctly with default value
    args = parser.parse_args([])
    assert args.become_user == None

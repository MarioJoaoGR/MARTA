
import argparse
from ansible.cli.arguments.option_helpers import add_runtask_options

def test_add_runtask_options():
    # Create an argument parser
    parser = argparse.ArgumentParser()
    
    # Add run task options to the parser
    add_runtask_options(parser)
    
    # Test adding a single extra variable 'foo=bar'
    args1 = parser.parse_args(['--extra-vars', 'foo=bar'])
    assert hasattr(args1, 'extra_vars') and args1.extra_vars == ['foo=bar']
    
    # Create an argument parser again to reset the state
    parser = argparse.ArgumentParser()
    add_runtask_options(parser)
    
    # Test adding multiple extra variables from command line arguments
    args2 = parser.parse_args(['--extra-vars', 'foo=bar', '--extra-vars', 'baz=qux'])
    assert hasattr(args2, 'extra_vars') and args2.extra_vars == ['foo=bar', 'baz=qux']
    
    # Create an argument parser again to reset the state
    parser = argparse.ArgumentParser()
    add_runtask_options(parser)
    
    # Test adding extra variables from a YAML file
    args3 = parser.parse_args(['--extra-vars', '@variables.yml'])
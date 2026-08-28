
import argparse
import pytest
from ansible.cli.arguments.option_helpers import UnrecognizedArgument

# Test valid inputs scenario
def test_valid_inputs():
    parser = argparse.ArgumentParser(description="Test script with unrecognized argument handling.")
    example_arg = UnrecognizedArgument(option_strings=['--example'], dest='example', help='An example argument')
    parser._actions.insert(0, example_arg)  # Insert at the beginning to ensure it catches all unrecognized arguments

    with pytest.raises(SystemExit):
        parser.parse_args(['--invalid'])

# Test edge cases scenario
def test_edge_cases():
    parser = argparse.ArgumentParser(description="Test script with unrecognized argument handling.")
    unrecognized_arg = UnrecognizedArgument(option_strings=[None], dest='unrecognized', help=None)
    parser._actions.insert(0, unrecognized_arg)  # Insert at the beginning to ensure it catches all unrecognized arguments

    args = parser.parse_args([])
    assert getattr(args, 'unrecognized', None) is None

# Test invalid inputs scenario
def test_invalid_inputs():
    parser = argparse.ArgumentParser(description="Test script with unrecognized argument handling.")
    unrecognized_arg = UnrecognizedArgument(option_strings=['--invalid'], dest='unrecognized', help='Unrecognized argument example')
    parser._actions.insert(0, unrecognized_arg)  # Insert at the beginning to ensure it catches all unrecognized arguments

    with pytest.raises(SystemExit):
        parser.parse_args(['--invalid'])

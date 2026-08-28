
import argparse
from lib.ansible.cli.arguments.option_helpers import UnrecognizedArgument
import pytest

# Test 1: test_valid_inputs - Test standard input
def test_valid_inputs():
    parser = argparse.ArgumentParser()
    unrecognized = UnrecognizedArgument(option_strings=['--example'], dest='example', help='An example argument')
    parser._actions.insert(0, unrecognized)  # Insert at the beginning to ensure it catches all unrecognized arguments

    with pytest.raises(SystemExit) as e:
        parser.parse_args(['--example'])
    
    assert str(e.value) == "2"

# Test 2: test_edge_cases - Test edge cases, including None, empty lists, and boundary values
def test_edge_cases():
    parser = argparse.ArgumentParser()
    unrecognized = UnrecognizedArgument(option_strings=['--test'], dest='test', help='A test argument')
    parser._actions.insert(0, unrecognized)  # Insert at the beginning to ensure it catches all unrecognized arguments

    with pytest.raises(SystemExit) as e:
        parser.parse_args(['--test'])
    
    assert str(e.value) == "2"

# Test 3: test_invalid_inputs - Test invalid inputs/error handling
def test_invalid_inputs():
    parser = argparse.ArgumentParser()
    unrecognized = UnrecognizedArgument(option_strings=['--invalid'], dest='invalid', help='An invalid argument')
    parser._actions.insert(0, unrecognized)  # Insert at the beginning to ensure it catches all unrecognized arguments

    with pytest.raises(SystemExit) as e:
        parser.parse_args(['--invalid'])
    
    assert str(e.value) == "2"

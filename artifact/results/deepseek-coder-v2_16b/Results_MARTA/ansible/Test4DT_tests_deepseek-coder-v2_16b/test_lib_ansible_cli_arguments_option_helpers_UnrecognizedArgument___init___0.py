
import argparse
import pytest
from ansible.cli.arguments.option_helpers import UnrecognizedArgument

def test_valid_inputs():
    parser = argparse.ArgumentParser()
    unrecognized = UnrecognizedArgument(option_strings=['--example'], dest='example', help='An example argument')
    parser._actions.insert(0, unrecognized)  # Insert at the beginning to ensure it catches all unrecognized arguments

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(['--example'])
    
    assert excinfo.value.code == 2

def test_edge_cases():
    parser = argparse.ArgumentParser()
    unrecognized = UnrecognizedArgument(option_strings=None, dest='example', help='An example argument')
    parser._actions.insert(0, unrecognized)  # Insert at the beginning to ensure it catches all unrecognized arguments

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args([])
    
    assert excinfo.value.code == 2

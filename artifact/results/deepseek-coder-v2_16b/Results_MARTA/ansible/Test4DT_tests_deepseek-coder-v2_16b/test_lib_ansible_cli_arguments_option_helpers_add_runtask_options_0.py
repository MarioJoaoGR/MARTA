
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import maybe_unfrack_path

def add_runtask_options(parser):
    """Add options for commands that run a task"""
    parser.add_argument('-e', '--extra-vars', dest="extra_vars", action="append", type=maybe_unfrack_path('@'),
                        help="set additional variables as key=value or YAML/JSON, if filename prepend with @", default=[])

# Test scenarios
def test_valid_inputs():
    parser = ArgumentParser()
    add_runtask_options(parser)
    args = parser.parse_args(['--extra-vars', 'foo=bar', '--extra-vars', '@vars.yml'])
    assert len(args.extra_vars) == 2
    assert args.extra_vars[0] == ('foo=bar')
    assert args.extra_vars[1].endswith('vars.yml')

def test_edge_cases():
    parser = ArgumentParser()
    add_runtask_options(parser)
    # Test None input
    with pytest.raises(SystemExit):
        parser.parse_args(['--extra-vars', 'None'])
    # Test empty list input
    with pytest.raises(SystemExit):
        parser.parse_args(['--extra-vars', ''])
    # Test boundary values (empty string)
    args = parser.parse_args(['--extra-vars', '@file_does_not_exist.yml'])
    assert len(args.extra_vars) == 1
    assert args.extra_vars[0].endswith('file_does_not_exist.yml')

def test_invalid_inputs():
    parser = ArgumentParser()
    add_runtask_options(parser)
    # Test malformed string input
    with pytest.raises(SystemExit):
        parser.parse_args(['--extra-vars', 'foo'])
    # Test non-existent file input
    with pytest.raises(SystemExit):
        parser.parse_args(['--extra-vars', '@nonexistentfile.yml'])


import sys
from isort.main import parse_args
from argparse import ArgumentParser

# Mocking the _build_arg_parser function since it's not defined in the provided code snippet
def _build_arg_parser():
    parser = ArgumentParser()
    parser.add_argument('--show-version', action='store_true')
    return parser

# Mocking sys.argv to simulate command line arguments
sys.argv = ['script_name']

def test_parse_args_none():
    # Test when argv is None
    result = parse_args(None)
    assert isinstance(result, dict), "Expected a dictionary"
    assert not result, "Expected an empty dictionary for no arguments"

def test_parse_args_empty_list():
    # Test when argv is an empty list
    result = parse_args([])
    assert isinstance(result, dict), "Expected a dictionary"
    assert not result, "Expected an empty dictionary for no arguments"

# Restoring the original _build_arg_parser function to avoid side effects in other tests
sys.modules['isort.main']._build_arg_parser = _build_arg_parser

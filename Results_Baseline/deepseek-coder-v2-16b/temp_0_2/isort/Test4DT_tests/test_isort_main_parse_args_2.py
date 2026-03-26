
import sys
from argparse import ArgumentParser
from typing import Any, Sequence

import pytest

from isort.main import parse_args


# Mocking the _build_arg_parser function since it's not defined in the provided code snippet
def _build_arg_parser():
    parser = ArgumentParser()
    parser.add_argument('--order_by_type', action='store_true')
    parser.add_argument('--follow_links', action='store_true')
    parser.add_argument('--dont_order_by_type', action='store_false', dest='order_by_type')
    parser.add_argument('--dont_follow_links', action='store_false', dest='follow_links')
    parser.add_argument('--float_to_top', action='store_true')
    parser.add_argument('--dont_float_to_top', action='store_false', dest='float_to_top')
    parser.add_argument('--multi_line_output', type=int, choices=[10, 20, 30])
    return parser

# Mocking the DEPRECATED_SINGLE_DASH_ARGS since it's not defined in the provided code snippet
DEPRECATED_SINGLE_DASH_ARGS = ['dont_order_by_type', 'dont_follow_links']

def test_parse_args_default():
    sys.argv[1:] = []  # Resetting command-line arguments to empty list
    args = parse_args()
    assert isinstance(args, dict)
    assert "order_by_type" not in args

import argparse
from constants import C
import pytest

def add_fork_options(parser):
    """Add options for commands that can fork worker processes"""
    parser.add_argument('-f', '--forks', dest='forks', default=C.DEFAULT_FORKS, type=int,
                        help="specify number of parallel processes to use (default=%s)" % C.DEFAULT_FORKS)

@pytest.fixture
def setup_parser():
    parser = argparse.ArgumentParser()
    add_fork_options(parser)
    return parser

# Test scenario 1: test_valid_input
def test_valid_input(setup_parser):
    args = setup_parser.parse_args(['--forks', '4'])
    assert args.forks == 4

# Test scenario 2: test_edge_case
def test_edge_case(setup_parser):
    args = setup_parser.parse_args([])
    assert args.forks == C.DEFAULT_FORKS

# Test scenario 3: test_invalid_input
def test_invalid_input(setup_parser):
    with pytest.raises(SystemExit) as excinfo:
        setup_parser.parse_args(['--forks', 'invalid'])
    assert excinfo.type == SystemExit


import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_async_options



def test_edge_cases():
    """Test edge cases for poll interval and background run settings."""
    parser = ArgumentParser()
    add_async_options(parser)
    
    args = parser.parse_args(['--poll', '0'])
    assert args.poll_interval == 0
    
    args = parser.parse_args(['--background', '0'])
    assert args.seconds == 0
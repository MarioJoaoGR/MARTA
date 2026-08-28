
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_async_options
import ansible.constants as C

def test_add_async_options():
    parser = ArgumentParser()
    add_async_options(parser)
    
    # Test default values
    args = parser.parse_args([])
    assert args.poll_interval == C.DEFAULT_POLL_INTERVAL
    assert args.seconds == 0

def test_add_async_options_with_custom_values():
    parser = ArgumentParser()
    add_async_options(parser)
    
    # Test custom values
    args = parser.parse_args(['-P', '120'])
    assert args.poll_interval == 120
    assert args.seconds == 0

def test_add_async_options_with_background():
    parser = ArgumentParser()
    add_async_options(parser)
    
    # Test background option with custom seconds value
    args = parser.parse_args(['-B', '3600'])
    assert args.poll_interval == C.DEFAULT_POLL_INTERVAL
    assert args.seconds == 3600

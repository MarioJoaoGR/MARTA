
import pytest
import argparse
from ansible.cli.arguments.option_helpers import add_meta_options


def test_add_meta_options_with_force_handlers():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args(['--force-handlers'])
    
    assert hasattr(args, 'force_handlers')
    assert args.force_handlers is True

def test_add_meta_options_with_flush_cache():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args(['--flush-cache'])
    
    assert hasattr(args, 'flush_cache')
    assert args.flush_cache is True
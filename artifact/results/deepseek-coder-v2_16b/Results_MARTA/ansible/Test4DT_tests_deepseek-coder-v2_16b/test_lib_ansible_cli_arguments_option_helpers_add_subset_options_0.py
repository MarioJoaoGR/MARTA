
import argparse
import pytest
from ansible.cli.arguments.option_helpers import add_subset_options

def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    args = parser.parse_args([])
    
    assert hasattr(args, 'tags'), "Expected argument 'tags' to be added"
    assert hasattr(args, 'skip_tags'), "Expected argument 'skip_tags' to be added"
    assert getattr(args, 'tags', None) == [], "Default value for tags should be an empty list"
    assert getattr(args, 'skip_tags', None) == [], "Default value for skip_tags should be an empty list"

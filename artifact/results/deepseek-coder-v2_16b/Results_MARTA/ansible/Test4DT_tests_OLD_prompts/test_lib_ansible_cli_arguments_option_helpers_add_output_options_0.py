
import pytest
from ansible.cli.arguments.option_helpers import add_output_options


def test_add_output_options_default():
    """Test that the default value for '--tree' is None."""
    from argparse import ArgumentParser
    
    # Create a mock argument parser
    parser = ArgumentParser()
    
    # Call the function under test
    add_output_options(parser)
    
    # Check that the default value for '--tree' is None
    args = parser.parse_args([])
    assert args.tree is None, "The default value for '--tree' should be None."


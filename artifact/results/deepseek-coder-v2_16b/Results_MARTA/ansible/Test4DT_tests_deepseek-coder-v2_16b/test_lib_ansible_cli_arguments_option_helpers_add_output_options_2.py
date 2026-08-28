
import argparse
import pytest

def add_output_options(parser):
    """Add options for commands which can change their output"""
    parser.add_argument('-o', '--one-line', dest='one_line', action='store_true', help='condense output')
    parser.add_argument('-t', '--tree', dest='tree', default=None, help='log output to this directory')

# Test scenarios
def test_valid_inputs():
    # Create an ArgumentParser instance and add the output options
    parser = argparse.ArgumentParser(description="Example script with output options")
    add_output_options(parser)
    
    # Parse arguments with valid inputs
    args = parser.parse_args(['-o', '-t', '/path/to/logdir'])
    
    # Assert expected results
    assert args.one_line is True
    assert args.tree == '/path/to/logdir'

def test_edge_cases():
    # Create an ArgumentParser instance and add the output options
    parser = argparse.ArgumentParser(description="Example script with output options")
    add_output_options(parser)
    
    # Parse arguments without any inputs (should use default values)
    args = parser.parse_args([])
    
    # Assert expected results for edge cases
    assert args.one_line is False
    assert args.tree is None

def test_invalid_inputs():
    # Create an ArgumentParser instance and add the output options
    parser = argparse.ArgumentParser(description="Example script with output options")
    add_output_options(parser)
    
    # Parse arguments with invalid inputs (incorrect flags)
    with pytest.raises(SystemExit):
        args = parser.parse_args(['-x'])  # Incorrect flag '-x'

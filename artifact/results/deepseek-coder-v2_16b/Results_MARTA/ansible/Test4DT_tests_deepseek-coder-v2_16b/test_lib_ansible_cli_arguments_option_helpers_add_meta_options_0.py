
import argparse
import pytest
from your_module import add_meta_options  # Replace 'your_module' with the actual module name where this function is defined

# Define a simple constant for testing
class C:
    DEFAULT_FORCE_HANDLERS = False

def test_valid_inputs():
    parser = argparse.ArgumentParser(description="Test command")
    add_meta_options(parser)
    args = parser.parse_args(['--force-handlers', '--flush-cache'])
    
    assert args.force_handlers is True
    assert args.flush_cache is True

def test_edge_cases():
    # No arguments provided
    parser = argparse.ArgumentParser(description="Test command")
    add_meta_options(parser)
    args = parser.parse_args([])
    
    assert args.force_handlers is False
    assert args.flush_cache is False
    
    # Only '--force-handlers' provided
    parser = argparse.ArgumentParser(description="Test command")
    add_meta_options(parser)
    args = parser.parse_args(['--force-handlers'])
    
    assert args.force_handlers is True
    assert args.flush_cache is False
    
    # Only '--flush-cache' provided
    parser = argparse.ArgumentParser(description="Test command")
    add_meta_options(parser)
    args = parser.parse_args(['--flush-cache'])
    
    assert args.force_handlers is False
    assert args.flush_cache is True
    
    # Invalid argument name provided
    with pytest.raises(SystemExit):
        parser = argparse.ArgumentParser(description="Test command")
        add_meta_options(parser)
        args = parser.parse_args(['--invalid-arg'])

def test_invalid_inputs():
    # Incorrect argument type provided
    with pytest.raises(SystemExit):
        parser = argparse.ArgumentParser(description="Test command")
        add_meta_options(parser)
        args = parser.parse_args(['--force-handlers', 'extra'])
    
    # Unsupported flag provided
    with pytest.raises(SystemExit):
        parser = argparse.ArgumentParser(description="Test command")
        add_meta_options(parser)
        args = parser.parse_args(['--no-such-flag'])

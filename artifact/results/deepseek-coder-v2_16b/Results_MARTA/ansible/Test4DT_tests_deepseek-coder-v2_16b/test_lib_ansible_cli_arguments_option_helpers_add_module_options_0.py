
import pytest
import argparse
from ansible.cli.arguments.option_helpers import add_module_options

def test_add_module_options_without_default():
    """Test adding module options without specifying default values."""
    parser = argparse.ArgumentParser(description="Command to load modules")
    add_module_options(parser)
    args = parser.parse_args([])
    assert hasattr(args, 'module_path'), "Expected 'module_path' argument to be added without a default value."
    assert getattr(args, 'module_path') is None, "Expected 'module_path' argument to have no default value."

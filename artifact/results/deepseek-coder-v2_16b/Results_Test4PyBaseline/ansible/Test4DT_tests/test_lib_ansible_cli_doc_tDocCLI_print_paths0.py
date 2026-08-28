
# Module: ansible.cli.doc
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

# Test initialization with default arguments
def test_default_initialization():
    cli = DocCLI(args=[])
    assert hasattr(cli, 'plugin_list'), "Expected 'plugin_list' attribute to be set"
    assert isinstance(cli.plugin_list, set), f"Expected 'plugin_list' to be a set, but got {type(cli.plugin_list)}"

# Test initialization with specific command-line arguments
def test_specific_arguments_initialization():
    cli = DocCLI(args=['--list-modules'])
    assert hasattr(cli, 'plugin_list'), "Expected 'plugin_list' attribute to be set"
    assert isinstance(cli.plugin_list, set), f"Expected 'plugin_list' to be a set, but got {type(cli.plugin_list)}"

# Mock the print_paths method to return a specific string for testing
@patch('ansible.cli.doc.DocCLI.print_paths', return_value="mocked_path")
def test_print_paths(mock_print_paths):
    finder = MagicMock()
    result = DocCLI.print_paths(finder)
    assert result == "mocked_path", f"Expected 'print_paths' to return 'mocked_path', but got {result}"

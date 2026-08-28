
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI
import os
from ansible.module_utils._text import to_text

# Test print_paths with a finder that returns multiple unique paths
def test_print_paths_multiple_unique():
    finder = MagicMock()
    finder._get_paths.return_value = ['/path1', '/path2', '/path3']
    result = DocCLI.print_paths(finder)
    assert result == os.pathsep.join(['/path1', '/path2', '/path3']), f"Expected paths to be joined with {os.pathsep}, but got {result}"

# Test print_paths with a finder that returns duplicate paths
def test_print_paths_duplicate_paths():
    finder = MagicMock()
    finder._get_paths.return_value = ['/path1', '/path2', '/path1']
    result = DocCLI.print_paths(finder)
    assert result == os.pathsep.join(['/path1', '/path2']), f"Expected paths to be joined without duplicates, but got {result}"

# Test print_paths with a finder that returns empty list
def test_print_paths_empty_list():
    finder = MagicMock()
    finder._get_paths.return_value = []
    result = DocCLI.print_paths(finder)
    assert result == os.pathsep.join([]), f"Expected an empty string for no paths, but got {result}"

# Test print_paths with a finder that returns paths containing surrogate or strict errors
def test_print_paths_surrogate_or_strict():
    finder = MagicMock()
    finder._get_paths.return_value = ['/path1', '/path2\ud800', '/path3']
    result = DocCLI.print_paths(finder)
    expected = os.pathsep.join(['/path1', to_text('/path2\ud800', errors='surrogate_or_strict'), '/path3'])
    assert result == expected, f"Expected paths to be converted with surrogate or strict error handling, but got {result}"

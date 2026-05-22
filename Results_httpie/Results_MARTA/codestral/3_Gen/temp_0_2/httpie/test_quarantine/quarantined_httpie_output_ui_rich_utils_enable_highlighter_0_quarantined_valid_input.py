
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_utils import Console, Highlighter

def enable_highlighter(console: Console, highlighter: Highlighter):
    """Enable a highlighter temporarily."""
    original_highlighter = console.highlighter
    try:
        console.highlighter = highlighter
        yield console
    finally:
        console.highlighter = original_highlighter

def test_valid_input():
    # Create a mock Console instance
    class MockConsole:
        def __init__(self):
            self.highlighter = None

    # Create a mock Highlighter instance
    class MockHighlighter:
        pass

    # Initialize the mock Console and Highlighter instances
    console = MockConsole()
    highlighter = MockHighlighter()

    # Use the enable_highlighter context manager to test its functionality
    with patch.object(MockConsole, 'highlighter', new=None):
        assert console.highlighter is None
        with enable_highlighter(console, highlighter) as enhanced_console:
            assert enhanced_console.highlighter == highlighter
        assert console.highlighter == highlighter

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_input.py:32:8: E1129: Context manager 'generator' doesn't implement __enter__ and __exit__. (not-context-manager)


"""
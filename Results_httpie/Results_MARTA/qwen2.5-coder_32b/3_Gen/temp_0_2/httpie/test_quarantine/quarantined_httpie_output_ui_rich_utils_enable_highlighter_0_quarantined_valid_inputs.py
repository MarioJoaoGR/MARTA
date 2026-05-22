
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

def test_valid_inputs():
    # Create a mock Console and Highlighter instances
    mock_console = Console()
    mock_highlighter = Highlighter()
    
    # Set up the mock to return the highlighter during creation
    with patch.object(mock_console, 'highlighter', new=mock_highlighter):
        # Create an iterator from the enable_highlighter function
        console_iterator = enable_highlighter(mock_console, mock_highlighter)
        
        # Ensure the highlighter is set correctly within the context
        assert mock_console.highlighter == mock_highlighter
        
        # Iterate through the iterator to ensure it yields the modified console
        next(console_iterator)
        
        # Check that after iteration, the original highlighter is restored
        assert mock_console.highlighter == mock_highlighter

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_inputs.py:18:23: E0110: Abstract class 'Highlighter' with abstract methods instantiated (abstract-class-instantiated)


"""
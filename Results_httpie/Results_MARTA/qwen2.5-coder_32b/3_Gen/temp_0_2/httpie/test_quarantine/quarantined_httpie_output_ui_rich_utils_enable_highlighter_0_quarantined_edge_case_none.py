
import pytest
from unittest.mock import patch, MagicMock
from console import Console
from highlighters import Highlighter, SimpleHighlighter

def enable_highlighter(console: Console, highlighter: Highlighter) -> Iterator[Console]:
    """Enable a highlighter temporarily."""
    original_highlighter = console.highlighter
    try:
        console.highlighter = highlighter
        yield console
    finally:
        console.highlighter = original_highlighter

def test_edge_case_none():
    # Create a mock Console instance
    mock_console = MagicMock()
    
    # Create a Highlighter instance
    my_highlighter = SimpleHighlighter()
    
    with patch('console.Console.highlighter', new_callable=MagicMock) as mock_highlighter:
        # Set up the mock highlighter to return the original highlighter for testing
        mock_highlighter.return_value = my_highlighter
        
        # Use the enable_highlighter context manager
        with enable_highlighter(mock_console, my_highlighter) as enhanced_console:
            assert enhanced_console.highlighter == my_highlighter
    
    # After the context, the original highlighter should be restored
    assert mock_console.highlighter == my_highlighter

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_case_none
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_case_none.py:4:0: E0401: Unable to import 'console' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_case_none.py:5:0: E0401: Unable to import 'highlighters' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_case_none.py:7:70: E0602: Undefined variable 'Iterator' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_case_none.py:28:8: E1129: Context manager 'generator' doesn't implement __enter__ and __exit__. (not-context-manager)


"""
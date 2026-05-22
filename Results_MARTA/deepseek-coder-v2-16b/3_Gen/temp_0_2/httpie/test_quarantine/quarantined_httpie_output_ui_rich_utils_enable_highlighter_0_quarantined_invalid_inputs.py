
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_utils import enable_highlighter
from console import Console
from highlighters import Highlighter, SimpleHighlighter

def test_enable_highlighter():
    # Create a mock Console and Highlighter instances
    mock_console = Console()
    mock_highlighter = SimpleHighlighter()
    
    with patch('console.Console.highlighter', new_callable=lambda: None):
        assert isinstance(mock_console.highlighter, type(None))
        
        # Use the enable_highlighter context manager to temporarily replace and restore the highlighter
        with enable_highlighter(mock_console, mock_highlighter) as enhanced_console:
            assert isinstance(enhanced_console.highlighter, Highlighter)
            
        # After the context, the original highlighter should be restored
        assert isinstance(mock_console.highlighter, type(None))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_rich_utils_enable_highlighter_0_test_invalid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_invalid_inputs.py:5:0: E0401: Unable to import 'console' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_invalid_inputs.py:6:0: E0401: Unable to import 'highlighters' (import-error)


"""

import pytest
from unittest.mock import patch, MagicMock
from console import Console
from highlighters import Highlighter

@pytest.fixture
def mock_console():
    console = MagicMock()
    yield console
    # Ensure the original state is restored after the test
    console.highlighter = None

def test_enable_highlighter(mock_console):
    highlighter = MagicMock()
    
    with patch('console.Console.highlighter', new_callable=MagicMock) as mock_highlighter:
        # Set up the mock to return the original highlighter during the yield
        mock_highlighter.return_value = mock_console.highlighter
        
        with enable_highlighter(mock_console, highlighter) as enhanced_console:
            assert enhanced_console == mock_console
            # Ensure the highlighter is temporarily replaced
            assert enhanced_console.highlighter == highlighter
    
    # After the context, ensure the original highlighter is restored
    assert mock_console.highlighter == mock_highlighter.return_value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_inputs.py:4:0: E0401: Unable to import 'console' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_inputs.py:5:0: E0401: Unable to import 'highlighters' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_inputs.py:21:13: E0602: Undefined variable 'enable_highlighter' (undefined-variable)


"""
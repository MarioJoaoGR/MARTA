
import pytest
from unittest.mock import patch, MagicMock
from console import Console
from highlighters import Highlighter

@pytest.fixture
def mock_console():
    console = MagicMock()
    yield console
    # Ensure the original state is restored after each test
    console.highlighter = None

def test_enable_highlighter(mock_console):
    highlighter = Highlighter()
    
    with patch('console.Console.highlighter', new_callable=MagicMock) as mock_highlighter:
        # Set up the mock to return the original highlighter when accessed
        mock_highlighter.return_value = None
        
        with enable_highlighter(mock_console, highlighter):
            assert mock_console.highlighter == highlighter
            
        assert mock_console.highlighter == None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_rich_utils_enable_highlighter_1_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_utils_enable_highlighter_1_test_edge_cases.py:4:0: E0401: Unable to import 'console' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_utils_enable_highlighter_1_test_edge_cases.py:5:0: E0401: Unable to import 'highlighters' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_utils_enable_highlighter_1_test_edge_cases.py:21:13: E0602: Undefined variable 'enable_highlighter' (undefined-variable)


"""
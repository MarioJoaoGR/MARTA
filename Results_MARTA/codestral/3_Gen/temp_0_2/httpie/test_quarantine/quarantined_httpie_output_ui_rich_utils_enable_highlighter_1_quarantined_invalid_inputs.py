
from httpie.output.ui.rich_utils import Console, Highlighter
from unittest.mock import patch
import pytest

def test_invalid_inputs():
    with patch('httpie.output.ui.rich_utils.Console') as MockConsole, \
         patch('httpie.output.ui.rich_utils.Highlighter') as MockHighlighter:
        mock_console = MockConsole()
        mock_highlighter = MockHighlighter()

        with pytest.raises(TypeError):
            enable_highlighter(mock_console, mock_highlighter)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_rich_utils_enable_highlighter_1_test_invalid_inputs
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_utils_enable_highlighter_1_test_invalid_inputs.py:13:12: E0602: Undefined variable 'enable_highlighter' (undefined-variable)


"""
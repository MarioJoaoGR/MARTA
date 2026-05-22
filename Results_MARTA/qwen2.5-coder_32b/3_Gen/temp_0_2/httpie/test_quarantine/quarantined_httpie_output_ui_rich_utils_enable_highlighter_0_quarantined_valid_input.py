
import unittest.mock as mock
from httpie.output.ui.rich_utils import enable_highlighter
from console import Console
from highlighters import Highlighter

def test_valid_input():
    # Create a mock Console instance
    my_console = mock.Mock(spec=Console)
    
    # Create a mock Highlighter instance
    my_highlighter = mock.Mock(spec=Highlighter)
    
    # Patch the highlighter attribute of the mock Console to return the mock Highlighter during yield
    with mock.patch.object(my_console, 'highlighter', new=my_highlighter):
        enhanced_console = next(enable_highlighter(my_console, my_highlighter))
        
        # Assert that the highlighter was temporarily enabled and then restored
        assert my_console.highlighter == my_highlighter

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_input.py:4:0: E0401: Unable to import 'console' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_input.py:5:0: E0401: Unable to import 'highlighters' (import-error)


"""
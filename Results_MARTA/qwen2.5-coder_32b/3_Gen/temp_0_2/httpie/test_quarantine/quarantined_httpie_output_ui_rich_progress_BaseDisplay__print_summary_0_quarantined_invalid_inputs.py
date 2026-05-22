
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.ui.rich_progress import BaseDisplay

class TestBaseDisplay(unittest.TestCase):
    @patch('httpie.output.ui.rich_progress.filesize')
    def test_print_summary_invalid_inputs(self, mock_filesize):
        base_display = BaseDisplay()
        
        # Mock the filesize module to return a fixed value for total_size and avg_speed
        mock_filesize.decimal.return_value = "1000 B"
        
        # Test with invalid inputs: negative time_spent, zero observed_steps
        base_display._print_summary(is_finished=True, observed_steps=-1, time_spent=-1)
        self.assertEqual(base_display.console.print.call_args[0][0], "Done. 0 B in -1:00:00 (-inf/s)")
        
        # Test with invalid inputs: zero observed_steps
        base_display._print_summary(is_finished=False, observed_steps=0, time_spent=0)
        self.assertEqual(base_display.console.print.call_args[0][0], "Interrupted. 0 B in 0:00:00 (0.0/s)")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_ui_rich_progress_BaseDisplay__print_summary_0_test_invalid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_BaseDisplay__print_summary_0_test_invalid_inputs.py:9:23: E1120: No value for argument 'env' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_BaseDisplay__print_summary_0_test_invalid_inputs.py:16:25: E1101: Method 'print' has no 'call_args' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_BaseDisplay__print_summary_0_test_invalid_inputs.py:20:25: E1101: Method 'print' has no 'call_args' member (no-member)


"""
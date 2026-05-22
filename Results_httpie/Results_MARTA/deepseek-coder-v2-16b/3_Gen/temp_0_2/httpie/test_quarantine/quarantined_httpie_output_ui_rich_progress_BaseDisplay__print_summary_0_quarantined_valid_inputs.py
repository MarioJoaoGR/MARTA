
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_progress import BaseDisplay

@pytest.fixture
def setup_base_display():
    return BaseDisplay()

def test_print_summary(setup_base_display):
    with patch('httpie.output.ui.rich_progress.filesize.decimal') as mock_decimal:
        mock_decimal.return_value = "1000"
        setup_base_display._print_summary(is_finished=True, observed_steps=1000, time_spent=3600)
        expected_output = 'Done. 1000 in 01:40:00.00000 (0.28/s)'
        assert setup_base_display.console.print.call_args[0][0] == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_rich_progress_BaseDisplay__print_summary_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_progress_BaseDisplay__print_summary_0_test_valid_inputs.py:8:11: E1120: No value for argument 'env' in constructor call (no-value-for-parameter)


"""
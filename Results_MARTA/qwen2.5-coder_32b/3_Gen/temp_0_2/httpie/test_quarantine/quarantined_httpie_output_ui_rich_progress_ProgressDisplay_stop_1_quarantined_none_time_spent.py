
from unittest.mock import patch, MagicMock
import pytest
from httpie.output.ui.rich_progress import ProgressDisplay

class TestProgressDisplayStop:
    @patch('httpie.output.ui.rich_progress.ProgressDisplay')
    def test_none_time_spent(self, MockProgressDisplay):
        progress_display = MockProgressDisplay()
        
        # Create a mock task with finished=True and completed=10 (or any non-zero value)
        task = MagicMock()
        task.finished = True
        task.completed = 10
        progress_display.progress_bar.tasks = [task]
        
        progress_display.stop(time_spent=None)
        
        # Add assertions to verify the expected behavior after calling stop with time_spent=None
        assert progress_display.progress_bar.stopped, "The progress bar should be stopped"
        assert progress_display.last_printed_summary is None, "No summary should be printed when time_spent is None"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_ProgressDisplay_stop_1_test_none_time_spent.py F [100%]

=================================== FAILURES ===================================
_________________ TestProgressDisplayStop.test_none_time_spent _________________

self = <test_httpie_output_ui_rich_progress_ProgressDisplay_stop_1_test_none_time_spent.TestProgressDisplayStop object at 0x7f67a760a5d0>
MockProgressDisplay = <MagicMock name='ProgressDisplay' id='140083161807440'>

    @patch('httpie.output.ui.rich_progress.ProgressDisplay')
    def test_none_time_spent(self, MockProgressDisplay):
        progress_display = MockProgressDisplay()
    
        # Create a mock task with finished=True and completed=10 (or any non-zero value)
        task = MagicMock()
        task.finished = True
        task.completed = 10
        progress_display.progress_bar.tasks = [task]
    
        progress_display.stop(time_spent=None)
    
        # Add assertions to verify the expected behavior after calling stop with time_spent=None
        assert progress_display.progress_bar.stopped, "The progress bar should be stopped"
>       assert progress_display.last_printed_summary is None, "No summary should be printed when time_spent is None"
E       AssertionError: No summary should be printed when time_spent is None
E       assert <MagicMock name='ProgressDisplay().last_printed_summary' id='140083161963920'> is None
E        +  where <MagicMock name='ProgressDisplay().last_printed_summary' id='140083161963920'> = <MagicMock name='ProgressDisplay()' id='140083161911248'>.last_printed_summary

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_ProgressDisplay_stop_1_test_none_time_spent.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_ProgressDisplay_stop_1_test_none_time_spent.py::TestProgressDisplayStop::test_none_time_spent
============================== 1 failed in 0.22s ===============================
"""
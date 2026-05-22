
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.ui.rich_progress import ProgressDisplay

@pytest.fixture(autouse=True)
def mock_progress_display():
    with patch('httpie.output.ui.rich_progress.ProgressDisplay') as MockClass:
        mock_instance = MockClass.return_value
        mock_instance.progress_bar = MagicMock()
        mock_instance.progress_bar.tasks = [MagicMock()]
        yield mock_instance

def test_valid_input(mock_progress_display):
    task = mock_progress_display.progress_bar.tasks[0]
    task.finished = True
    task.completed = 100
    
    mock_progress_display.stop(time_spent=3600)
    
    assert mock_progress_display.progress_bar.stop.called
    assert mock_progress_display._print_summary.called
    assert mock_progress_display._print_summary.call_args[1]['is_finished'] == True
    assert mock_progress_display._print_summary.call_args[1]['observed_steps'] == 100
    assert mock_progress_display._print_summary.call_args[1]['time_spent'] == 3600

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_ProgressDisplay_stop_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

mock_progress_display = <MagicMock name='ProgressDisplay()' id='139711107364752'>

    def test_valid_input(mock_progress_display):
        task = mock_progress_display.progress_bar.tasks[0]
        task.finished = True
        task.completed = 100
    
        mock_progress_display.stop(time_spent=3600)
    
>       assert mock_progress_display.progress_bar.stop.called
E       AssertionError: assert False
E        +  where False = <MagicMock name='ProgressDisplay().progress_bar.stop' id='139711084525392'>.called
E        +    where <MagicMock name='ProgressDisplay().progress_bar.stop' id='139711084525392'> = <MagicMock name='ProgressDisplay().progress_bar' id='139711104997136'>.stop
E        +      where <MagicMock name='ProgressDisplay().progress_bar' id='139711104997136'> = <MagicMock name='ProgressDisplay()' id='139711107364752'>.progress_bar

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_ProgressDisplay_stop_0_test_valid_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_progress_ProgressDisplay_stop_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.22s ===============================
"""
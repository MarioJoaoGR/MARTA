
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_progress import StatusDisplay

def test_valid_input():
    with patch('httpie.output.ui.rich_progress.StatusDisplay') as mock_status_display:
        status_display = mock_status_display.return_value
        status_display.description = 'Operation completed'
        status_display.observed = 1000
        
        status_display.stop(time_spent=3600)
        
        assert status_display.console.print.called_with('Operation completed')
        assert status_display._print_summary.called_with(is_finished=True, observed_steps=1000, time_spent=3600)

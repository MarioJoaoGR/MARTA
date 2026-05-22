
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.ui.rich_progress import ProgressDisplay

def test_invalid_input():
    with patch('httpie.output.ui.rich_progress.ProgressDisplay', autospec=True) as mock_progress_display:
        progress_bar = MagicMock()
        tasks = [MagicMock(finished=False, completed=10)]
        progress_bar.tasks = tasks
        mock_progress_display.return_value.progress_bar = progress_bar
        
        with pytest.raises(TypeError):
            progress_display = mock_progress_display()
            progress_display.stop(time_spent="non-numeric value")

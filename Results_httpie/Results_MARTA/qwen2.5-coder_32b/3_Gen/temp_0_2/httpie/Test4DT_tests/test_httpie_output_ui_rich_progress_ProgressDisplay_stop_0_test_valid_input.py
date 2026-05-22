
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.ui.rich_progress import ProgressDisplay

@pytest.fixture
def mock_progress_display():
    with patch('httpie.output.ui.rich_progress.ProgressDisplay') as MockClass:
        mock_instance = MockClass.return_value
        yield mock_instance

def test_valid_input(mock_progress_display):
    task = mock_progress_display.progress_bar.tasks[0]
    task.finished = True
    task.completed = 100
    
    with patch.object(mock_progress_display, 'stop') as stop_mock:
        mock_progress_display.stop(time_spent=3600)
        
        assert stop_mock.called

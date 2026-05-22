
from unittest.mock import patch, MagicMock
import pytest
from httpie.output.ui.rich_progress import ProgressDisplay

class TestProgressDisplayStop:
    @patch('httpie.output.ui.rich_progress.ProgressDisplay')
    def test_edge_case_none(self, MockProgressDisplay):
        # Create an instance of the mocked ProgressDisplay class
        progress_display = MockProgressDisplay()
        
        # Mock the necessary attributes and methods on the progress_bar object
        mock_progress_bar = MagicMock()
        mock_task = MagicMock()
        mock_task.completed = 100
        mock_task.finished = True
        mock_progress_bar.tasks = [mock_task]
        
        # Assign the mocked progress_bar to the progress_display instance
        progress_display.progress_bar = mock_progress_bar
        
        # Call the stop method with a time_spent value
        progress_display.stop(time_spent=3600)
        
        # Add assertions to verify the behavior
        assert progress_display.progress_bar.tasks[0].completed == 100
        assert progress_display.progress_bar.tasks[0].finished is True

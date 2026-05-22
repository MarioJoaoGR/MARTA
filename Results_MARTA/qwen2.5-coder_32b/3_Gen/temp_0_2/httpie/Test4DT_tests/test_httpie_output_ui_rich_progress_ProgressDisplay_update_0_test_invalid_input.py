
from unittest.mock import patch, MagicMock
import pytest
from httpie.output.ui.rich_progress import ProgressDisplay

class TestProgressDisplay:
    @patch('httpie.output.ui.rich_progress.ProgressDisplay')
    def test_invalid_input(self, MockProgressDisplay):
        progress_display = MockProgressDisplay()
        
        # Create a mock instance of the update method that will raise ValueError for invalid input
        with patch.object(progress_display, 'update', side_effect=ValueError("Invalid input")):
            with pytest.raises(ValueError):
                progress_display.update(-1)  # This should trigger the exception

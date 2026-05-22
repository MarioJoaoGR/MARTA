
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_progress import ProgressDisplay

@pytest.mark.parametrize("steps", [0, 0.5, 1])
def test_update(steps):
    with patch('httpie.output.ui.rich_progress.ProgressDisplay') as mock_progress_display:
        instance = mock_progress_display.return_value
        instance.transfer_task = None  # Assuming transfer_task is a property or method that should be mocked if needed
        instance.update(steps)
        assert instance.progress_bar.advance.called_with(instance.transfer_task, steps)

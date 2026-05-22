
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_progress import StatusDisplay

@pytest.fixture
def status_display():
    with patch('httpie.output.ui.rich_progress.StatusDisplay') as mock_status_display:
        yield mock_status_display

def test_invalid_input(status_display):
    # Assuming the constructor of StatusDisplay takes no parameters, we don't need to pass any arguments here.
    status_display_instance = status_display()
    
    # Now you can use status_display_instance in your tests as needed.

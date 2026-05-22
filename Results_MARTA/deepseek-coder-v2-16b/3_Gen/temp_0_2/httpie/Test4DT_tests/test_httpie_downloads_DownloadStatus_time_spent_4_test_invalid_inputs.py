
import pytest
from datetime import datetime, timedelta
from unittest.mock import patch

class DownloadStatus:
    """Holds details about the download status."""
    def __init__(self, env):
        self.env = env
        self.downloaded = 0
        self.total_size = None
        self.resumed_from = 0
        self.time_started = None
        self.time_finished = None

    def time_spent(self):
        if (
            self.time_started is not None
            and self.time_finished is not None
        ):
            return self.time_finished - self.time_started
        else:
            return None

@pytest.fixture
def setup():
    env = "network_storage"
    status = DownloadStatus(env)
    status.downloaded = 1024
    status.total_size = 102400
    status.resumed_from = 0
    status.time_started = None
    return status

def test_invalid_inputs(setup):
    with patch('datetime.datetime') as mock_datetime:
        # Mock the datetime now and timedelta functions to control the time flow
        mock_now = datetime.now()
        setup.time_started = mock_now
        
        # Test when time_finished is not set
        assert setup.time_spent() is None
        
        # Set a future time for time_finished to simulate completion after start
        future_time = mock_now + timedelta(hours=1)
        setup.time_finished = future_time
        
        # Test when both time_started and time_finished are set
        assert isinstance(setup.time_spent(), timedelta)
        
        # Reset for the next test
        setup.time_finished = None
        
        # Test when only time_started is set (should return None)
        assert setup.time_spent() is None

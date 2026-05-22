
import pytest
from unittest.mock import patch
from datetime import datetime, timedelta

class DownloadStatus:
    """Holds details about the download status."""
    def __init__(self, env):
        self.env = env
        self.downloaded = 0
        self.total_size = None
        self.resumed_from = 0
        self.time_started = None
        self.time_finished = None

    def terminate(self, time_spent=None):
        if hasattr(self, 'display'):
            self.display.stop(self.time_spent)

@pytest.fixture
def setup_download_status():
    return DownloadStatus(env="test_env")

def test_valid_input(setup_download_status):
    status = setup_download_status
    assert status.env == "test_env"
    assert status.downloaded == 0
    assert status.total_size is None
    assert status.resumed_from == 0
    assert status.time_started is None
    assert status.time_finished is None

    # Mock the time_started attribute to simulate a started download
    with patch('datetime.datetime') as mock_datetime:
        now = datetime.now()
        mock_datetime.now.return_value = now
        status.time_started = now
        
        assert status.time_started == now

    # Mock the time_finished attribute to simulate a finished download
    with patch('datetime.datetime') as mock_datetime:
        later = datetime.now() + timedelta(seconds=10)
        mock_datetime.now.return_value = later
        status.time_finished = later
        
        assert status.time_finished == later

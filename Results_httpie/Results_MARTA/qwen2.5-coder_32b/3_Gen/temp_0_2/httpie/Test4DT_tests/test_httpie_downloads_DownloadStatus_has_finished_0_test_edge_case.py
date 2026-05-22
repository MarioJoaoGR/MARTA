
import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock

class DownloadStatus:
    """Holds details about the download status."""
    def __init__(self, env):
        self.env = env
        self.downloaded = 0
        self.total_size = None
        self.resumed_from = 0
        self.time_started = None
        self.time_finished = None

    def has_finished(self):
        return self.time_finished is not None

def test_edge_case():
    with patch('datetime.datetime') as mock_datetime:
        # Mocking datetime now to ensure consistent time for testing
        mock_now = MagicMock()
        mock_datetime.now.return_value = mock_now
        
        status = DownloadStatus(env='network_storage')
        status.downloaded = 1024
        status.total_size = None
        status.resumed_from = 0
        status.time_started = datetime.now()
        status.time_finished = None
        
        assert not status.has_finished(), "Expected download to be unfinished"
        
        # Setting time finished to a mock value for the test assertion
        mock_now.replace = MagicMock(return_value=datetime(2023, 10, 15))
        status.time_finished = datetime(2023, 10, 15)
        
        assert status.has_finished(), "Expected download to be finished after setting time_finished"

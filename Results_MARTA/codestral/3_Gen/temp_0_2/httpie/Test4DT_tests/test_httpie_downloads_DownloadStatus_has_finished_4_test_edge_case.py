
import pytest
from unittest.mock import patch
from datetime import datetime

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
        # Mock the datetime now function to always return a fixed time
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        
        status = DownloadStatus(env='network_storage')
        status.time_finished = None
        status.total_size = None
        
        assert not status.has_finished(), "Expected download to be in progress"
        
        # Set time_finished to a fixed datetime value
        mock_datetime.now.return_value = datetime(2023, 1, 2)
        status.time_finished = mock_datetime.now()
        
        assert status.has_finished(), "Expected download to be finished"


import pytest
from unittest.mock import patch, MagicMock
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

    def finished(self):
        assert self.time_started is not None
        assert self.time_finished is None
        self.time_finished = datetime.now()
        if hasattr(self, 'display'):
            self.display.stop(self.time_spent)

@pytest.fixture
def download_status():
    return DownloadStatus(env="test_env")

def test_edge_case(download_status):
    with patch('builtins.print'):  # Mocking print to prevent output in tests
        with pytest.raises(AssertionError):
            download_status.finished()
        
        download_status.time_started = datetime.now()
        download_status.finished()
        assert download_status.time_finished is not None

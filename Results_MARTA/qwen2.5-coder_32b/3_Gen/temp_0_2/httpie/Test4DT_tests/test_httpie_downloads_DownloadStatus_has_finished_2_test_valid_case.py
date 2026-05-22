
import pytest
from datetime import datetime
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

    def has_finished(self):
        return self.time_finished is not None

@pytest.fixture
def setup_download_status():
    status = DownloadStatus(env='network_storage')
    status.downloaded = 1024
    status.total_size = 102400
    status.resumed_from = 0
    status.time_started = datetime.now()
    return status

def test_valid_case(setup_download_status):
    assert setup_download_status.env == 'network_storage'
    assert setup_download_status.downloaded == 1024
    assert setup_download_status.total_size == 102400
    assert setup_download_status.resumed_from == 0
    assert setup_download_status.time_started is not None
    assert setup_download_status.has_finished() == False

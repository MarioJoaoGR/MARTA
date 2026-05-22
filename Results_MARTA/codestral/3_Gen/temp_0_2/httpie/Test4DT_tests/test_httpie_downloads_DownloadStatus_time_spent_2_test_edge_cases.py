
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
    env = 'network_storage'
    status = DownloadStatus(env)
    status.downloaded = 1024
    status.total_size = 102400
    status.resumed_from = 0
    return status

def test_time_spent_none(setup):
    with patch('datetime.datetime') as mock_datetime:
        now = datetime.now()
        mock_datetime.now.return_value = now
        
        setup.time_started = now
        assert setup.time_spent() is None

def test_time_spent_with_finish(setup):
    with patch('datetime.datetime') as mock_datetime:
        start_time = datetime.now()
        finish_time = start_time + timedelta(seconds=10)
        mock_datetime.now.side_effect = [start_time, finish_time]
        
        setup.time_started = start_time
        setup.time_finished = finish_time
        assert setup.time_spent() == timedelta(seconds=10)

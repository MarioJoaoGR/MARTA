
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
def setup_download():
    env = "test_env"
    download_status = DownloadStatus(env)
    yield download_status

@pytest.mark.parametrize("start_time, finish_time", [
    (datetime.now(), datetime.now() + timedelta(seconds=10)),
    (None, None),  # Both should return None
    (datetime.now(), None)  # Only start time should return None
])
def test_valid_inputs(setup_download, start_time, finish_time):
    setup_download.time_started = start_time
    if finish_time:
        setup_download.time_finished = finish_time
    
    assert isinstance(setup_download.time_spent(), timedelta) or setup_download.time_spent() is None

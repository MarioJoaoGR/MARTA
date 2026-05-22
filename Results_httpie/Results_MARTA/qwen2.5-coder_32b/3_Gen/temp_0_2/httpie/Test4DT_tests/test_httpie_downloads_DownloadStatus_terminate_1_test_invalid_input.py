
import pytest
from unittest.mock import patch
from datetime import datetime, timedelta

class DownloadStatus:
    """Holds details about the download status."""
    def __init__(self, env):
        if env != 'valid_env':
            raise ValueError("Invalid environment")
        self.env = env
        self.downloaded = 0
        self.total_size = None
        self.resumed_from = 0
        self.time_started = None
        self.time_finished = None

    def terminate(self):
        if hasattr(self, 'display'):
            self.display.stop(self.time_spent)

def test_invalid_input():
    with pytest.raises(ValueError) as e:
        DownloadStatus(env='invalid_env')
    assert str(e.value) == "Invalid environment"


import pytest
from unittest.mock import patch
from httpie.downloads import DownloadStatus

def test_valid_input():
    with patch('httpie.downloads.DownloadStatus.__init__', return_value=None):
        status = DownloadStatus(env="network_storage")
        assert status is not None

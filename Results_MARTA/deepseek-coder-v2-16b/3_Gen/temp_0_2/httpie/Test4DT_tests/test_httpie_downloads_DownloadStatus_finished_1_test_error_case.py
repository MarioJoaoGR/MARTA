
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus

def test_error_case():
    with patch('httpie.downloads.DownloadStatus', autospec=True):
        status = DownloadStatus(env="test_env")
        with pytest.raises(AssertionError):
            status.finished()


import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus

@pytest.fixture
def valid_download_status():
    return DownloadStatus(env="test_env")

def test_valid_input(valid_download_status):
    with patch('httpie.downloads.DownloadStatus.start_display') as mock_start_display:
        output_file = MagicMock()
        valid_download_status.total_size = 102400
        valid_download_status.downloaded = 51200
        valid_download_status.start_display(output_file)
        mock_start_display.assert_called_once_with(output_file)

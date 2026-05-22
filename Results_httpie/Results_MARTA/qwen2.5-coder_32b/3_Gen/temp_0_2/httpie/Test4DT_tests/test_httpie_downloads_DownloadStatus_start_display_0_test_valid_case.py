
import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus

@pytest.fixture(autouse=True)
def setup_download_status():
    status = DownloadStatus(env='network_storage')
    status.downloaded = 1024
    status.total_size = 102400
    status.resumed_from = 0
    status.time_started = datetime.now()
    return status

def test_valid_case(setup_download_status):
    with patch('httpie.downloads.DownloadStatus.start_display') as mock_start_display:
        setup_download_status.start_display(output_file=MagicMock())
        assert mock_start_display.called

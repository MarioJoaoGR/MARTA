
import pytest
from unittest.mock import patch
from httpie.downloads import DownloadStatus

@pytest.fixture(autouse=True)
def setup_download_status():
    status = DownloadStatus(env=None)
    status.total_size = None
    status.resumed_from = 0
    return status

def test_edge_case(setup_download_status):
    with patch('httpie.downloads.DownloadStatus.start_display') as mock_start_display:
        setup_download_status.start_display(output_file='dummy_file')
        assert mock_start_display.called

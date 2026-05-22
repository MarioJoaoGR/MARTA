
import pytest
from unittest.mock import patch
from httpie.downloads import DownloadStatus

@pytest.fixture(autouse=True)
def setup_download_status():
    status = DownloadStatus(env='network_storage')
    status.total_size = 1024 * 1024
    status.downloaded = 512 * 1024
    yield status

@pytest.mark.parametrize("output_file", [open('valid_output', 'wb')])
def test_valid_case(setup_download_status, output_file):
    with patch('httpie.downloads.DownloadStatus.start_display'):
        setup_download_status.start_display(output_file)
        assert setup_download_status.total_size == 1024 * 1024
        assert setup_download_status.downloaded == 512 * 1024

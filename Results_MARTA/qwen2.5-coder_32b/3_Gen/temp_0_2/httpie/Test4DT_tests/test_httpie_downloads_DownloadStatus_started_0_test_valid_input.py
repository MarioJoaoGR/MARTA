
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus

@pytest.fixture
def status():
    return DownloadStatus(env='test')

def test_valid_input(status):
    with patch('httpie.downloads.DownloadStatus.start_display', new=MagicMock()):
        output_file = MagicMock()
        output_file.name = 'downloaded_file'
        status.started(output_file, resumed_from=0, total_size=None)
        assert status.time_started is not None
        assert status.total_size is None
        assert status.resumed_from == 0


import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus

@pytest.fixture
def mock_environment():
    return Environment(config={"network": "example.com"})

@pytest.fixture
def mock_output_file():
    return MagicMock()

@pytest.fixture
def downloader(mock_environment, mock_output_file):
    return Downloader(env=mock_environment, output_file=mock_output_file, resume=True)

def test_failed_method(downloader):
    with patch('httpie.downloads.DownloadStatus.terminate') as mock_terminate:
        downloader.failed()
        assert not downloader.finished
        mock_terminate.assert_called_once()

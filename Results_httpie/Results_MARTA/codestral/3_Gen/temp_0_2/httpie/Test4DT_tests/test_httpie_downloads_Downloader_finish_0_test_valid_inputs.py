
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus

@pytest.fixture
def setup_downloader():
    env = Environment(config={"network": "example.com"})
    output_file = MagicMock()
    downloader = Downloader(env=env, output_file=output_file, resume=False)
    return downloader

def test_finish(setup_downloader):
    downloader = setup_downloader
    with patch.object(DownloadStatus, 'finished', new_callable=MagicMock) as mock_finished:
        downloader.finish()
        assert downloader.finished
        mock_finished.assert_called_once()


import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, DownloadStatus

@pytest.fixture
def setup_downloader():
    env = MagicMock()
    output_file = MagicMock()
    downloader = Downloader(env=env, output_file=output_file, resume=True)
    return downloader

def test_valid_chunk_downloaded(setup_downloader):
    downloader = setup_downloader
    chunk = b'some data'
    
    with patch.object(DownloadStatus, 'chunk_downloaded') as mock_chunk_downloaded:
        downloader.chunk_downloaded(chunk)
        assert mock_chunk_downloaded.call_count == 1
        args, _ = mock_chunk_downloaded.call_args
        assert args[0] == len(chunk)

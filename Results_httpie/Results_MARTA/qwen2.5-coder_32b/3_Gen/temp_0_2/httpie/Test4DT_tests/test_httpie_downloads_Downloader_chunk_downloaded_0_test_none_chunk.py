
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader

@pytest.fixture
def downloader():
    env = MagicMock()
    output_file = MagicMock()
    return Downloader(env=env, output_file=output_file)

def test_chunk_downloaded(downloader):
    chunk = b'data'
    with patch('httpie.downloads.DownloadStatus.chunk_downloaded') as mock_chunk_downloaded:
        downloader.chunk_downloaded(chunk)
        assert mock_chunk_downloaded.called
        args, _ = mock_chunk_downloaded.call_args
        assert args[0] == len(chunk)

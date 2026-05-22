
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader

@pytest.fixture
def downloader():
    env = MagicMock()
    output_file = MagicMock()
    return Downloader(env=env, output_file=output_file, resume=True)

def test_none_chunk(downloader):
    with patch('httpie.downloads.DownloadStatus.chunk_downloaded') as mock_chunk_downloaded:
        chunk = b'some_data'
        downloader.chunk_downloaded(chunk)
        mock_chunk_downloaded.assert_called_with(len(chunk))

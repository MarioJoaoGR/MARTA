
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.downloader.http import HttpFD
from youtube_dl.downloader.common import FileDownloader


def test_invalid_input():
    with patch('youtube_dl.downloader.http.HttpFD') as MockHttpFD:
        mock_instance = MockHttpFD.return_value
        mock_instance.real_download = MagicMock(side_effect=Exception("HTTP 405 Method Not Allowed"))

        params = {
            'url': 'http://example.com/video.mp4',
            'http_headers': {'User-Agent': 'Mozilla/5.0'},
            'retries': 3,
            'verbose': True,
            'http_chunk_size': 8192,
            'method': 'INVALID'  # Unsupported HTTP method
        }

        with pytest.raises(Exception):
            FileDownloader(ydl=None, params=params).real_download('output_file.mp4', params)
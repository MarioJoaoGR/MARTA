
import pytest
from unittest.mock import MagicMock
from youtube_dl.downloader.common import FileDownloader


def test_report_progress():
    ydl = MagicMock()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }
    downloader = FileDownloader(ydl, params)
    with pytest.raises(TypeError):
        downloader.report_progress(1, 10, 50.0)
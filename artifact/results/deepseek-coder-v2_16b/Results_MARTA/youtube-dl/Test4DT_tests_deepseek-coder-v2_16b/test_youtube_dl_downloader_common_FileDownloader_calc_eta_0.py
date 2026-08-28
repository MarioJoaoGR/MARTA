
import pytest
from youtube_dl.downloader.common import FileDownloader
import time

# Test for invalid rate limit input

# Test for valid rate limit input
def test_valid_rate_limit():
    ydl = None  # Assuming ydl is properly initialized elsewhere in the codebase
    params = {
        'verbose': True,
        'ratelimit': 10240,  # Valid rate limit (positive)
        'retries': 3,
        'buffersize': 8192,  # Valid buffer size
        'test': False
    }
    downloader = FileDownloader(ydl, params)

    start_time = time.time() - 3600  # One hour ago
    now_time = time.time()
    total_size = 1024 * 1024  # 1 MB
    downloaded_size = 512 * 1024  # Half a MB

    eta = FileDownloader.calc_eta(start_time, now_time, total_size, downloaded_size)
    assert isinstance(eta, int), "Expected an integer ETA"
    assert eta > 0, "Expected positive ETA for partial download"
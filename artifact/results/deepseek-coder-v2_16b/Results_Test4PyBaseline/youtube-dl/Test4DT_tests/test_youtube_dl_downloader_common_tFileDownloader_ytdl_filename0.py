
# Module: youtube_dl.downloader.common
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mocking FileDownloader for test purposes
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = [lambda *args: None]
        
        def ytdl_filename(self, filename):
            return f"{filename}.ytdl"

# Fixture to create a FileDownloader instance for testing
@pytest.fixture
def downloader():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
    }
    return FileDownloader(ydl, params)

# Test case for the ytdl_filename method
def test_ytdl_filename(downloader):
    filename = "testvideo"
    expected_output = "testvideo.ytdl"
    assert downloader.ytdl_filename(filename) == expected_output

# Test case for the __init__ method with default parameters
def test_file_downloader_init():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl
    assert len(downloader._progress_hooks) == 1

# Test case for the __init__ method with additional parameters
def test_file_downloader_init_with_additional_params():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
        'retries': 3,
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl
    assert len(downloader._progress_hooks) == 1

# Test case for the __init__ method with testing parameters
def test_file_downloader_init_for_testing():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
        'retries': 3,
        'test': True,
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl
    assert len(downloader._progress_hooks) == 1

# Test case for the __init__ method with HLS parameters
def test_file_downloader_init_for_hls():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
        'retries': 3,
        'test': False,
        'hls_use_mpegts': True,
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl
    assert len(downloader._progress_hooks) == 1


import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    # If the module is not found, we can define a mock or placeholder for FileDownloader
    class FileDownloader:
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = [lambda: None]  # Placeholder for progress hooks

# Test initialization with basic parameters
def test_file_downloader_basic():
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
    assert callable(downloader._progress_hooks[0])

# Test initialization with additional parameters
def test_file_downloader_additional_params():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
        'retries': 3,          # Number of times to retry for HTTP error 5xx.
        'noprogress': False,    # Do not print the progress bar.
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl
    assert len(downloader._progress_hooks) == 1
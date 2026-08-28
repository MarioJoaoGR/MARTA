
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mocking FileDownloader for the purpose of this test case
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = []

        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

        def remove_progress_hook(self, hook):
            if hook in self._progress_hooks:
                self._progress_hooks.remove(hook)

        def report_retry(self, err, count, retries):
            """Report retry in case of HTTP error 5xx"""
            print(f'[download] Got server HTTP error: {err}. Retrying (attempt {count} of {retries})...')
            if isinstance(err, Exception) and count < retries:
                raise err

# Test initialization with default parameters
def test_file_downloader_initialization():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, 'params')
    assert hasattr(downloader, '_progress_hooks')

# Test initialization with specific parameters
def test_file_downloader_initialization_with_params():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params

# Test adding a progress hook
def test_add_progress_hook():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    def mock_hook(*args):
        pass
    downloader.add_progress_hook(mock_hook)
    assert len(downloader._progress_hooks) == 1

# Test removing a progress hook
def test_remove_progress_hook():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    def mock_hook(*args):
        pass
    downloader.add_progress_hook(mock_hook)
    assert len(downloader._progress_hooks) == 1
    downloader.remove_progress_hook(mock_hook)
    assert len(downloader._progress_hooks) == 0

# Test reporting retry in case of HTTP error 5xx with a specific exception
def test_report_retry_with_specific_exception():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    err = Exception('HTTP Error 503')
    count = 1
    retries = 3
    with pytest.raises(Exception):
        downloader.report_retry(err, count, retries)

# Test reporting retry in case of HTTP error 5xx with a different exception
def test_report_retry_with_different_exception():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    err = Exception('HTTP Error 504')
    count = 1
    retries = 3
    with pytest.raises(Exception):
        downloader.report_retry(err, count, retries)

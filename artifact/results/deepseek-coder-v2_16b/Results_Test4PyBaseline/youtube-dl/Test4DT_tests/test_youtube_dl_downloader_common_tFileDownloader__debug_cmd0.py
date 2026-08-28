
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:
        def __init__(self, ydl, params):
            self.ydl = ydl
            self._progress_hooks = []
            self.params = params
        
        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

# Test initialization with default parameters
def test_file_downloader_initialization():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, '_progress_hooks')
    assert hasattr(downloader, 'params')
    assert isinstance(downloader.ydl, YoutubeDL)
    assert isinstance(downloader._progress_hooks, list)
    assert isinstance(downloader.params, dict)

# Test initialization with verbose mode enabled
def test_file_downloader_initialization_with_verbose():
    ydl = YoutubeDL()
    params = {'verbose': True}
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'params')
    assert downloader.params['verbose'] is True

# Test initialization with specific parameters
def test_file_downloader_initialization_with_specific_params():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
    }
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'params')
    assert downloader.params['verbose'] is True
    assert downloader.params['ratelimit'] == 10240
    assert downloader.params['buffersize'] == 8192

# Test adding a progress hook
def test_file_downloader_add_progress_hook():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    def mock_progress_hook(*args):
        pass
    downloader.add_progress_hook(mock_progress_hook)
    assert len(downloader._progress_hooks) == 1
    assert downloader._progress_hooks[0] == mock_progress_hook

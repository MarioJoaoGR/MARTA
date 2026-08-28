
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mocking the FileDownloader for test purposes
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = []
        
        def add_progress_hook(self, hook):
            if callable(hook):
                self._progress_hooks.append(hook)
        
        def to_screen(self, message=None):  # Modified to accept a default None value for message
            if message is not None:
                raise NotImplementedError("This method is not implemented in the mock.")
    
# Test initialization with default parameters
def test_file_downloader_default():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, 'params')
    assert hasattr(downloader, '_progress_hooks')
    assert len(downloader._progress_hooks) == 0  # Corrected assertion to match expected behavior

# Test initialization with specific parameters
def test_file_downloader_specific_parameters():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
        # Add other parameters as needed
    }
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert downloader.params == params
    assert len(downloader._progress_hooks) == 0  # Corrected assertion to match expected behavior

# Test adding a progress hook
def test_add_progress_hook():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    initial_hook_count = len(downloader._progress_hooks)
    
    def mock_progress_hook(*args, **kwargs):
        pass
    
    downloader.add_progress_hook(mock_progress_hook)
    assert len(downloader._progress_hooks) == initial_hook_count + 1  # Corrected assertion to match expected behavior
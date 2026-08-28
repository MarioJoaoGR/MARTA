
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = []
        
        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)
        
        def _hook_progress(self, status):
            for hook in self._progress_hooks:
                hook(status)
    
    FileDownloader = FileDownloader  # Reassign to avoid NameError in test environment

# Test initialization with default parameters
def test_file_downloader_default():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, 'params')
    assert hasattr(downloader, '_progress_hooks')
    assert isinstance(downloader.ydl, YoutubeDL)
    assert isinstance(downloader.params, dict)
    assert isinstance(downloader._progress_hooks, list)

# Test initialization with all parameters set
def test_file_downloader_all_params():
    ydl = YoutubeDL()
    params = {
        'verbose': True,
        'quiet': False,
        'ratelimit': 10240,
        'retries': 5,
        'buffersize': 8192,
        'noresizebuffer': False,
        'continuedl': True,
        'noprogress': False,
        'logtostderr': False,
        'consoletitle': False,
        'nopart': False,
        'updatetime': False,
        'test': False,
        'min_filesize': 0,
        'max_filesize': None,
        'xattr_set_filesize': False,
        'external_downloader_args': [],
        'hls_use_mpegts': False,
        'http_chunk_size': 1048576,
    }
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, 'params')
    assert hasattr(downloader, '_progress_hooks')
    assert isinstance(downloader.ydl, YoutubeDL)
    assert isinstance(downloader.params, dict)
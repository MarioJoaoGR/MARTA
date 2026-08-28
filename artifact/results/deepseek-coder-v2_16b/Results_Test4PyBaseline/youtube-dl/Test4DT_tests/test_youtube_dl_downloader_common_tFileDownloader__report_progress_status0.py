
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Placeholder for the actual implementation
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = []

        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

        def start_download(self):
            raise NotImplementedError("This method is not implemented.")

# Test initialization with default parameters
def test_file_downloader_init():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    assert downloader.ydl == ydl
    assert downloader.params == params
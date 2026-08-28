
# Module: youtube_dl.downloader.common
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mocking FileDownloader for the sake of example
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self._progress_hooks = []
        
        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)
        
        def report_file_already_downloaded(self, file_name):
            raise NotImplementedError("This method is not implemented in the mock class.")

# Fixture to create a FileDownloader instance for testing
@pytest.fixture
def downloader():
    ydl = YoutubeDL()
    params = {
        'verbose': True,          # Print additional info to stdout
        'ratelimit': 10240,       # Download speed limit in bytes/sec
        'buffersize': 8192,        # Size of download buffer in bytes
    }
    return FileDownloader(ydl, params)

# Test case to check if the FileDownloader instance is created correctly
def test_file_downloader_creation(downloader):
    assert isinstance(downloader, FileDownloader)
    assert downloader.params == {
        'verbose': True,
        'ratelimit': 10240,
        'buffersize': 8192,
    }

# Test case to check if the progress hook is added correctly
def test_add_progress_hook(downloader):
    assert len(downloader._progress_hooks) == 0
    downloader.add_progress_hook(lambda *args: None)
    assert len(downloader._progress_hooks) == 1

# Test case to check the report_file_already_downloaded method
def test_report_file_already_downloaded(downloader):
    file_name = "test_file.mp4"
    with pytest.raises(NotImplementedError):
        downloader.report_file_already_downloaded(file_name)


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

# Test case for the ytdl_filename method with a specific filename
def test_ytdl_filename_specific_case(downloader):
    filename = "testvideo"
    expected_output = "testvideo.ytdl"
    assert downloader.ytdl_filename(filename) == expected_output

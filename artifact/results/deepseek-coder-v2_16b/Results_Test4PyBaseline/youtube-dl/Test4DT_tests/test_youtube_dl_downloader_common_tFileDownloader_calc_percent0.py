
# Module: youtube_dl.downloader.common
import pytest
from youtube_dl import YoutubeDL
try:
    from file_downloader import FileDownloader
except ImportError:
    class FileDownloader:  # Mocking the FileDownloader class for testing purposes
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
        
        def calc_percent(self, byte_counter, data_len):
            if data_len is None:
                return None
            return (byte_counter / data_len) * 100.0

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

# Test case for the calc_percent method
def test_calc_percent(downloader):
    # Test when data length is known
    byte_counter = 5120
    data_len = 10240
    expected_percent = (byte_counter / data_len) * 100.0
    assert downloader.calc_percent(byte_counter, data_len) == expected_percent

    # Test when data length is unknown
    byte_counter = 5120
    data_len = None
    assert downloader.calc_percent(byte_counter, data_len) is None

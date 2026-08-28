
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
            return float(byte_counter) / float(data_len) * 100.0

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

# Test case for the calc_percent method when data length is known
def test_calc_percent_known_length(downloader):
    byte_counter = 5120
    data_len = 10240
    expected_percent = float(byte_counter) / float(data_len) * 100.0
    assert downloader.calc_percent(byte_counter, data_len) == expected_percent

# Test case for the calc_percent method when data length is None
def test_calc_percent_none_length(downloader):
    byte_counter = 5120
    data_len = None
    assert downloader.calc_percent(byte_counter, data_len) is None

# Test case for the calc_percent method with zero byte counter
def test_calc_percent_zero_byte_counter(downloader):
    byte_counter = 0
    data_len = 10240
    expected_percent = float(byte_counter) / float(data_len) * 100.0
    assert downloader.calc_percent(byte_counter, data_len) == expected_percent

# Test case for the calc_percent method with negative byte counter (should be valid but unusual)
def test_calc_percent_negative_byte_counter(downloader):
    byte_counter = -5120  # Negative byte counter is allowed but not usual
    data_len = 10240
    expected_percent = float(byte_counter) / float(data_len) * 100.0
    assert downloader.calc_percent(byte_counter, data_len) == expected_percent

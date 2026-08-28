
import pytest
from youtube_dl.downloader.common import FileDownloader

# Test for invalid inputs to ensure it raises a TypeError
def test_invalid_inputs():
    # Assuming YTDL is a valid downloader object, but we don't use it directly in this test
    with pytest.raises(TypeError):
        FileDownloader()  # This should raise a TypeError because the constructor expects at least two arguments

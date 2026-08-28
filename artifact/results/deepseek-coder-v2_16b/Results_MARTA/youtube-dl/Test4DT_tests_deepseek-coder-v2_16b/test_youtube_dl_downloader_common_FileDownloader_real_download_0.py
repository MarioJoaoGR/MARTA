
import pytest
from youtube_dl.downloader.common import FileDownloader

# Test case for checking if FileDownloader can be instantiated without parameters
def test_no_params():
    ydl = None  # Assuming YTDL is a valid downloader object, but we don't use it directly in the test
    with pytest.raises(TypeError):
        FileDownloader(ydl=ydl)


import pytest
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def setup_file_downloader():
    ydl = None  # Assuming YTDL is a placeholder for the actual module or class
    params = {}
    return FileDownloader(ydl, params)

def test_edge_case(setup_file_downloader):
    downloader = setup_file_downloader
    with pytest.raises(TypeError):
        # Attempt to instantiate FileDownloader without any parameters should raise TypeError
        FileDownloader()

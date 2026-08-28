
import pytest
from youtube_dl.downloader.common import FileDownloader

def test_edge_case():
    ydl = "dummy_ydl"
    params = {}
    downloader = FileDownloader(ydl, params)
    
    with pytest.raises(AttributeError):
        # This should raise AttributeError because the function does not exist in FileDownloader
        downloader.test_edge_case()

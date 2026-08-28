
import pytest
from youtube_dl.downloader.common import FileDownloader

def test_calc_percent():
    # Test when data length is None
    assert FileDownloader.calc_percent(1024, None) is None
    
    # Test when byte counter and data length are valid numbers
    assert FileDownloader.calc_percent(5120, 10240) == 50.0
    
    # Test when byte counter and data length are equal
    assert FileDownloader.calc_percent(10240, 10240) == 100.0
    
    # Test when byte counter is zero but data length is valid
    assert FileDownloader.calc_percent(0, 10240) == 0.0


import pytest
from youtube_dl.downloader.fragment import FragmentFD

def test_valid_input():
    fd = FragmentFD(ydl='dummy_ydl', params={'dummy': 'params'})
    assert isinstance(fd, FragmentFD), "Expected an instance of FragmentFD"

def test_edge_case():
    fd = FragmentFD(ydl='dummy_ydl', params={'dummy': 'params'})
    assert isinstance(fd, FragmentFD), "Expected an instance of FragmentFD"

def test_invalid_input():
    with pytest.raises(TypeError):
        fd = FragmentFD()  # Missing ydl and params arguments


from youtube_dl.downloader.f4m import _add_ns
import pytest

def test_valid_input():
    result = _add_ns('title')
    assert result == '{http://ns.adobe.com/f4m/1.0}title'

def test_valid_input_with_version():
    result = _add_ns('description', 2)
    assert result == '{http://ns.adobe.com/f4m/2.0}description'

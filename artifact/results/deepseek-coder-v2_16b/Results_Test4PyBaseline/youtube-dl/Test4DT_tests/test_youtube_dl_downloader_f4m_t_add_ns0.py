# Module: youtube_dl.downloader.f4m
import pytest
from youtube_dl.downloader.f4m import _add_ns

# Test cases for _add_ns function

def test_default_version():
    assert _add_ns('video') == '{http://ns.adobe.com/f4m/1.0}video'

def test_explicit_version():
    assert _add_ns('video', 2) == '{http://ns.adobe.com/f4m/2.0}video'

def test_different_property_name():
    assert _add_ns('data') == '{http://ns.adobe.com/f4m/1.0}data'

# Additional edge cases and error handling can be added here if needed

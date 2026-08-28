
import pytest
from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl import YoutubeDL

# Test 1: Initialize PostProcessor without downloader
def test_init_without_downloader():
    post_processor = PostProcessor()
    assert hasattr(post_processor, '_downloader'), "PostProcessor instance should have a _downloader attribute"
    assert post_processor._downloader is None, "_downloader should be None if not provided during initialization"

# Test 2: Initialize PostProcessor with downloader
def test_init_with_downloader():
    my_downloader = YoutubeDL()
    post_processor = PostProcessor(downloader=my_downloader)
    assert hasattr(post_processor, '_downloader'), "PostProcessor instance should have a _downloader attribute"
    assert post_processor._downloader == my_downloader, "_downloader should be the provided downloader instance"

# Test 3: Initialize PostProcessor with invalid type for downloader
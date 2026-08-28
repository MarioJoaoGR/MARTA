
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl import YoutubeDL

# Test initialization without downloader
def test_init_without_downloader():
    post_processor = PostProcessor()
    assert hasattr(post_processor, '_downloader'), "PostProcessor instance should have a _downloader attribute"
    assert post_processor._downloader is None, "_downloader should be None if not provided during initialization"

# Test initialization with downloader
def test_init_with_downloader():
    mock_downloader = YoutubeDL()
    post_processor = PostProcessor(downloader=mock_downloader)
    assert hasattr(post_processor, '_downloader'), "PostProcessor instance should have a _downloader attribute"
    assert post_processor._downloader == mock_downloader, "_downloader should be the provided downloader instance"

# Test setting downloader after initialization
def test_set_downloader():
    post_processor = PostProcessor()
    mock_downloader = YoutubeDL()
    post_processor.set_downloader(mock_downloader)
    assert hasattr(post_processor, '_downloader'), "PostProcessor instance should have a _downloader attribute"
    assert post_processor._downloader == mock_downloader, "_downloader should be the provided downloader instance after setting it"

# Test invalid input to initialization (should raise TypeError)
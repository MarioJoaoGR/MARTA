
import pytest
from youtube_dl.postprocessor.common import PostProcessor
from unittest.mock import patch, MagicMock

# Test for initializing PostProcessor without a downloader
def test_init_without_downloader():
    post_processor = PostProcessor()
    assert hasattr(post_processor, '_downloader'), "PostProcessor instance should have an attribute _downloader"
    assert post_processor._downloader is None, "_downloader should be initialized to None if not provided"

# Test for initializing PostProcessor with a downloader
def test_init_with_downloader():
    mock_downloader = MagicMock()
    post_processor = PostProcessor(downloader=mock_downloader)
    assert hasattr(post_processor, '_downloader'), "PostProcessor instance should have an attribute _downloader"
    assert post_processor._downloader == mock_downloader, "_downloader should be set to the provided downloader"

# Test for retrieving configuration arguments without default value
def test_configuration_args_without_default():
    mock_downloader = MagicMock()
    mock_downloader.params = {'postprocessor_args': []}
    post_processor = PostProcessor(downloader=mock_downloader)
    assert post_processor._configuration_args() == [], "Configuration args should return an empty list if not provided"

# Test for retrieving configuration arguments with a default value
def test_configuration_args_with_default():
    mock_downloader = MagicMock()
    mock_downloader.params = {}
    post_processor = PostProcessor(downloader=mock_downloader)
    assert post_processor._configuration_args([1, 2, 3]) == [1, 2, 3], "Configuration args should return the default value if not provided in params"

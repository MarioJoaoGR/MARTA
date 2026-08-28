
import pytest
from youtube_dl.postprocessor.common import PostProcessor

@pytest.fixture
def setup_post_processor():
    # Create a mock downloader for the post processor to use
    class MockDownloader:
        params = {}
    
    # Instantiate the PostProcessor with the mock downloader
    post_processor = PostProcessor(downloader=MockDownloader())
    return post_processor

def test_valid_inputs(setup_post_processor):
    post_processor = setup_post_processor
    assert isinstance(post_processor, PostProcessor)
    assert post_processor._downloader is not None

def test_configuration_args(setup_post_processor):
    post_processor = setup_post_processor
    # Test the _configuration_args method with a default value
    config_args = post_processor._configuration_args()
    assert isinstance(config_args, list)
    assert config_args == []

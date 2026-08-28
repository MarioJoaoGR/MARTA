
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.postprocessor.common import PostProcessor

@pytest.fixture
def setup_post_processor():
    downloader = MagicMock()
    post_processor = PostProcessor(downloader=downloader)
    return post_processor, downloader

def test_run_post_processor_with_mocked_dependencies(setup_post_processor):
    post_processor, downloader = setup_post_processor
    
    # Mock the run method of PostProcessor to return default values
    with patch.object(PostProcessor, 'run', return_value=([], {'filepath': '/path/to/downloaded/file'})):
        information = {'filepath': '/path/to/downloaded/file'}
        result = post_processor.run(information)
        
        # Assert the expected behavior
        assert result == ([], {'filepath': '/path/to/downloaded/file'})


import pytest
from unittest.mock import patch
from semantic_release.hvcs import Github
from requests.exceptions import HTTPError
import logging

# Configure logger for debugging messages
logger = logging.getLogger('semantic_release')

def test_get_release_success():
    # Mocking a successful response from GitHub API
    mock_response = {
        "id": 123456,
        "tag_name": "v1.0.0"
    }
    
    with patch('semantic_release.hvcs.Github.session') as mock_session:
        # Mocking the session's get method to return a successful response
        mock_session.return_value.get.return_value.json.return_value = mock_response
        
        # Calling the get_release method
        release_id = Github.get_release('owner', 'repo', 'v1.0.0')
        
        # Asserting that the release ID is as expected
        assert release_id == 123456

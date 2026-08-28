
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github
from requests.exceptions import HTTPError
import logging

# Configure logger for the tests
logger = logging.getLogger('semantic_release')
logger.setLevel(logging.WARNING)  # Set to WARNING level so it only logs warnings and errors




def test_create_release_api_failure():
    mock_session = MagicMock()
    with patch('semantic_release.hvcs.Github.session', return_value=mock_session):
        mock_session.post.side_effect = HTTPError("API Error")
        result = Github.create_release('owner', 'repo', 'v1.0', 'Initial release notes')
        assert result is False, "Expected failure due to API error"
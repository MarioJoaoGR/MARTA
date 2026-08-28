
import pytest
from unittest.mock import patch, MagicMock
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

# Test scenarios
def test_valid_input():
    with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": 123456}
        mock_session = MagicMock()
        mock_session.get.return_value = mock_response
        
        with patch('semantic_release.hvcs.Github.session', return_value=mock_session):
            result = Github.get_release('owner', 'repo', 'tag')
            assert result == 123456

def test_missing_release():
    with patch('semantic_release.hvcs.Github.session', side_effect=HTTPError(response=MagicMock(status_code=404))):
        result = Github.get_release('owner', 'repo', 'tag')
        assert result is None

def test_invalid_input():
    with patch('semantic_release.hvcs.Github.session', side_effect=HTTPError(response=MagicMock(status_code=401))):
        result = Github.get_release('owner', 'repo', 'tag')
        assert result is None

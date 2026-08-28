
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github


def test_invalid_owner():
    with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
        mock_response = MagicMock()
        mock_response.json.return_value = {"state": "failure"}
        mock_session = MagicMock()
        mock_session.get.return_value = mock_response

        with patch('semantic_release.hvcs.Github.api_url', return_value='https://api.github.com'):
            assert Github.check_build_status('invalid-owner', 'repo', 'ref') is False

def test_invalid_repo():
    with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
        mock_response = MagicMock()
        mock_response.json.return_value = {"state": "success"}
        mock_session = MagicMock()
        mock_session.get.return_value = mock_response

        with patch('semantic_release.hvcs.Github.api_url', return_value='https://api.github.com'):
            assert Github.check_build_status('owner', 'invalid-repo', 'ref') is False

def test_invalid_ref():
    with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
        mock_response = MagicMock()
        mock_response.json.return_value = {"state": "success"}
        mock_session = MagicMock()
        mock_session.get.return_value = mock_response

        with patch('semantic_release.hvcs.Github.api_url', return_value='https://api.github.com'):
            assert Github.check_build_status('owner', 'repo', 'invalid-ref') is False
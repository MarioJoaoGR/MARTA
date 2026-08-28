
import pytest
from unittest.mock import patch, MagicMock
import requests
from semantic_release.hvcs import Github


def test_check_build_status_invalid_owner():
    with patch('semantic_release.hvcs.Github.session') as mock_session:
        mock_response = MagicMock()
        mock_response.json.return_value = {"state": "failure"}  # Assuming failure for invalid owner case
        mock_session.get.side_effect = requests.HTTPError("Invalid Owner")

        result = Github.check_build_status('invalid-owner', 'repo', 'ref')

        assert result is False

def test_check_build_status_invalid_repo():
    with patch('semantic_release.hvcs.Github.session') as mock_session:
        mock_response = MagicMock()
        mock_response.json.return_value = {"state": "pending"}  # Assuming pending for invalid repo case
        mock_session.get.side_effect = requests.HTTPError("Invalid Repo")

        result = Github.check_build_status('owner', 'invalid-repo', 'ref')

        assert result is False

def test_check_build_status_invalid_ref():
    with patch('semantic_release.hvcs.Github.session') as mock_session:
        mock_response = MagicMock()
        mock_response.json.return_value = {"state": "success"}  # Assuming success for invalid ref case
        mock_session.get.side_effect = requests.HTTPError("Invalid Ref")

        result = Github.check_build_status('owner', 'repo', 'invalid-ref')

        assert result is False
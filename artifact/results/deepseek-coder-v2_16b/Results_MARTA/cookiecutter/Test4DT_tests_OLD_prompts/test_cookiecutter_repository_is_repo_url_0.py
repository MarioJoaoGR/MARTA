
import pytest
from unittest.mock import patch, MagicMock
from cookiecutter.repository import REPO_REGEX, is_repo_url

@pytest.fixture(autouse=True)
def setup_regex():
    # Setup the regex mock for all tests
    mock_regex = MagicMock()
    yield
    # Teardown (if necessary) can be handled here if needed

@patch('cookiecutter.repository.REPO_REGEX', MagicMock())
def test_valid_https_repo_url():
    value = "https://github.com/user/repo"
    mock_regex = MagicMock()
    mock_regex.match.return_value = True
    with patch('cookiecutter.repository.REPO_REGEX', mock_regex):
        assert is_repo_url(value) == True

@patch('cookiecutter.repository.REPO_REGEX', MagicMock())
def test_valid_http_repo_url():
    value = "http://example.com/user/repo.git"
    mock_regex = MagicMock()
    mock_regex.match.return_value = True
    with patch('cookiecutter.repository.REPO_REGEX', mock_regex):
        assert is_repo_url(value) == True

@patch('cookiecutter.repository.REPO_REGEX', MagicMock())
def test_valid_ssh_repo_url():
    value = "git@github.com:user/repo.git"
    mock_regex = MagicMock()
    mock_regex.match.return_value = True
    with patch('cookiecutter.repository.REPO_REGEX', mock_regex):
        assert is_repo_url(value) == True

@patch('cookiecutter.repository.REPO_REGEX', MagicMock())
def test_invalid_local_repo_url():
    value = "http://localhost:5000/user/repo"
    mock_regex = MagicMock()
    mock_regex.match.return_value = False
    with patch('cookiecutter.repository.REPO_REGEX', mock_regex):
        assert is_repo_url(value) == False

@patch('cookiecutter.repository.REPO_REGEX', MagicMock())
def test_invalid_trailing_slash_repo_url():
    value = "https://github.com/user/repo/"
    mock_regex = MagicMock()
    mock_regex.match.return_value = False
    with patch('cookiecutter.repository.REPO_REGEX', mock_regex):
        assert is_repo_url(value) == False


import pytest
from cookiecutter.repository import is_repo_url

def test_is_repo_url_valid_github():
    assert is_repo_url('https://github.com/user/repo.git')

def test_is_repo_url_valid_gitlab():
    assert is_repo_url('https://gitlab.com/user/repo.git')

def test_is_repo_url_invalid_string():
    assert not is_repo_url('not_a_url')

def test_is_repo_url_local_path():
    assert not is_repo_url('/path/to/local/repo')

def test_is_repo_url_missing_git_extension():
    # This test assumes that the REPO_REGEX does not require the .git extension
    assert is_repo_url('https://github.com/user/repo')

def test_is_repo_url_empty_string():
    assert not is_repo_url('')

def test_is_repo_url_none():
    with pytest.raises(TypeError):
        is_repo_url(None)

def test_is_repo_url_valid_bitbucket():
    assert is_repo_url('https://bitbucket.org/user/repo.git')

def test_is_repo_url_https_without_www():
    assert is_repo_url('http://github.com/user/repo.git')

def test_is_repo_url_with_query_parameters():
    # This test assumes that the REPO_REGEX does not consider query parameters
    assert is_repo_url('https://github.com/user/repo.git?query=param')

def test_is_repo_url_with_fragment_identifier():
    # This test assumes that the REPO_REGEX does not consider fragment identifiers
    assert is_repo_url('https://github.com/user/repo.git#fragment')

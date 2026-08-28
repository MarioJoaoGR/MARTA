
import pytest
from cookiecutter.repository import is_repo_url

# Define a simple regex pattern for repository URLs for testing purposes.
# This should match typical git repository URLs.
REPO_REGEX = re.compile(
    r'^(https?|git)://[a-zA-Z0-9.-]+(/[a-zA-Z0-9._-]+)+(\.git)?$'
)

def test_none_repo_url():
    """Test that None is not considered a valid repository URL."""
    assert is_repo_url(None) is False

def test_empty_string_repo_url():
    """Test that an empty string is not considered a valid repository URL."""
    assert is_repo_url('') is False

def test_http_github_repo_url_with_git_suffix():
    """Test that an HTTP GitHub URL with .git suffix is considered a valid repository URL."""
    assert is_repo_url('http://github.com/user/repo.git') is True

def test_https_github_repo_url_with_git_suffix():
    """Test that an HTTPS GitHub URL with .git suffix is considered a valid repository URL."""
    assert is_repo_url('https://github.com/user/repo.git') is True

def test_http_github_repo_url_without_git_suffix():
    """Test that an HTTP GitHub URL without .git suffix is not considered a valid repository URL."""
    assert is_repo_url('http://github.com/user/repo') is False

def test_https_github_repo_url_without_git_suffix():
    """Test that an HTTPS GitHub URL without .git suffix is not considered a valid repository URL."""
    assert is_repo_url('https://github.com/user/repo') is False

def test_http_gitlab_repo_url_with_git_suffix():
    """Test that an HTTP GitLab URL with .git suffix is considered a valid repository URL."""
    assert is_repo_url('http://gitlab.com/user/repo.git') is True

def test_https_gitlab_repo_url_with_git_suffix():
    """Test that an HTTPS GitLab URL with .git suffix is considered a valid repository URL."""
    assert is_repo_url('https://gitlab.com/user/repo.git') is True

def test_http_bitbucket_repo_url_with_git_suffix():
    """Test that an HTTP Bitbucket URL with .git suffix is considered a valid repository URL."""
    assert is_repo_url('http://bitbucket.org/user/repo.git') is True

def test_https_bitbucket_repo_url_with_git_suffix():
    """Test that an HTTPS Bitbucket URL with .git suffix is considered a valid repository URL."""
    assert is_repo_url('https://bitbucket.org/user/repo.git') is True

def test_local_path_is_not_repo_url():
    """Test that a local path is not considered a valid repository URL."""
    assert is_repo_url('/path/to/local/template') is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________ ERROR collecting test_cookiecutter_repository_is_repo_url_0.py ________
/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_repository_is_repo_url_0.py:7: in <module>
    REPO_REGEX = re.compile(
E   NameError: name 're' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_repository_is_repo_url_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.22s ===============================
"""
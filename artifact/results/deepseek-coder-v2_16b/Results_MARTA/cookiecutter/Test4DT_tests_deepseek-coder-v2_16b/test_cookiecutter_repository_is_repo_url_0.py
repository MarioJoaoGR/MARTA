
import pytest
from cookiecutter.repository import is_repo_url

# Test for valid repository URL with HTTPS protocol
def test_valid_https_repo_url():
    value = "https://github.com/user/repo"
    assert is_repo_url(value) == True, f"Expected {value} to be a valid repository URL."

# Test for invalid repository URL with HTTP protocol but no trailing slash

# Test for valid repository URL with SSH protocol
def test_valid_ssh_repo_url():
    value = "git@github.com:user/repo.git"
    assert is_repo_url(value) == True, f"Expected {value} to be a valid repository URL."

# Test for invalid repository URL with HTTPS protocol and trailing slash

# Test for invalid repository URL with HTTP protocol and localhost address
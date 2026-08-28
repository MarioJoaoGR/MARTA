
import pytest
import os
from unittest.mock import patch

def gitlab(branch: str):
    """
    Checks if the current GitLab CI/CD environment's branch matches the specified branch.
    
    This function ensures that the build is intended for release creation by checking
    if the environment variable ``CI_COMMIT_REF_NAME`` matches the provided `branch` parameter.
    
    Parameters:
        branch (str): The name of the GitLab branch that the environment should be running against.
        
    Raises:
        AssertionError: If the value of ``CI_COMMIT_REF_NAME`` does not match the specified `branch`.
    """
    assert os.environ.get("CI_COMMIT_REF_NAME") == branch

@pytest.fixture(autouse=True)
def clean_env():
    if "CI_COMMIT_REF_NAME" in os.environ:
        del os.environ["CI_COMMIT_REF_NAME"]

# Test for valid input (happy path)
def test_valid_input_happy_path():
    with patch.dict(os.environ, {"CI_COMMIT_REF_NAME": "release"}):
        gitlab('release')

# Test for missing environment variable
def test_missing_env_var():
    with pytest.raises(AssertionError):
        gitlab('release')

# Test for invalid branch input
def test_invalid_branch_input():
    with patch.dict(os.environ, {"CI_COMMIT_REF_NAME": "non-release"}):
        with pytest.raises(AssertionError):
            gitlab('release')

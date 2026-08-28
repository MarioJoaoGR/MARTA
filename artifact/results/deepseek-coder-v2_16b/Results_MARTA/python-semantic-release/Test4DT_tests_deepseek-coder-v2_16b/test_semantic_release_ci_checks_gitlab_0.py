
import os
import pytest
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
def setup_env():
    # Save original environment variable and restore it after tests
    original_ci_commit_ref_name = os.environ.get("CI_COMMIT_REF_NAME", "default")
    yield  # Run the tests
    os.environ["CI_COMMIT_REF_NAME"] = original_ci_commit_ref_name

def test_valid_branch_match():
    with patch.dict(os.environ, {"CI_COMMIT_REF_NAME": "release"}):
        gitlab('release')

def test_invalid_branch():
    with patch.dict(os.environ, {"CI_COMMIT_REF_NAME": "wrong_branch"}):
        with pytest.raises(AssertionError):
            gitlab('release')

def test_missing_environment_variable():
    del os.environ['CI_COMMIT_REF_NAME']
    with pytest.raises(AssertionError):
        gitlab('release')

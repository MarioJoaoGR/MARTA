
import os
from unittest.mock import patch
import pytest

def travis(branch: str):
    """
    Performs necessary checks to ensure that the Travis build is one that should create releases.

    This function verifies that the current Travis branch matches the provided `branch` argument and that no pull request is being processed. It uses environment variables set by Travis CI to make these verifications.

    Parameters:
        branch (str): The name of the branch the environment should be running against. This must match the value of the ``TRAVIS_BRANCH`` environment variable for the function to pass.

    Raises:
        AssertionError: If the `branch` argument does not match the current Travis branch or if a pull request is detected (indicated by ``TRAVIS_PULL_REQUEST`` being "false").
    """
    assert os.environ.get("TRAVIS_BRANCH") == branch
    assert os.environ.get("TRAVIS_PULL_REQUEST") == "false"

@pytest.fixture(autouse=True)
def setup_travis_env():
    with patch.dict(os.environ, {"TRAVIS_BRANCH": "", "TRAVIS_PULL_REQUEST": ""}):
        yield

def test_valid_branch_match():
    with patch.dict(os.environ, {"TRAVIS_BRANCH": "main", "TRAVIS_PULL_REQUEST": "false"}):
        travis("main")

def test_invalid_branch_mismatch():
    with patch.dict(os.environ, {"TRAVIS_BRANCH": "not-main", "TRAVIS_PULL_REQUEST": "false"}):
        with pytest.raises(AssertionError):
            travis("main")

def test_pull_request_detected():
    with patch.dict(os.environ, {"TRAVIS_BRANCH": "main", "TRAVIS_PULL_REQUEST": "true"}):
        with pytest.raises(AssertionError):
            travis("main")

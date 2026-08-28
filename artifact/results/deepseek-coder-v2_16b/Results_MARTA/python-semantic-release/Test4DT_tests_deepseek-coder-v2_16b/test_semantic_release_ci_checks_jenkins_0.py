
import os
import pytest
from unittest.mock import patch

def jenkins(branch: str):
    """
    Performs necessary checks to ensure that the Jenkins build is one that should create releases.

    This function verifies that the environment's branch matches the specified branch, confirms the presence of a Jenkins URL in the environment variables, and ensures there is no pull request ID present.

    Parameters:
        branch (str): The branch name that the environment should be running against. This parameter is used to verify that the current branch matches this value.

    Raises:
        AssertionError: If any of the following conditions are not met:
            - The environment's branch does not match the specified `branch`.
            - The Jenkins URL is not found in the environment variables.
            - A pull request ID is present in the environment variables.
    """
    branch_name = os.environ.get("BRANCH_NAME") or os.environ.get("GIT_BRANCH")
    assert os.environ.get("JENKINS_URL") is not None
    assert branch_name == branch
    assert not os.environ.get("CHANGE_ID")  # pull request id

@pytest.fixture(autouse=True)
def setup_env():
    os.environ["BRANCH_NAME"] = "main"
    os.environ["JENKINS_URL"] = "http://valid-url.com"
    yield
    del os.environ["BRANCH_NAME"]
    del os.environ["JENKINS_URL"]

def test_valid_input_main_branch(setup_env):
    with patch('os.environ', {**os.environ, "BRANCH_NAME": "main", "JENKINS_URL": "http://valid-url.com"}):
        jenkins("main")

def test_invalid_branch(setup_env):
    with patch('os.environ', {**os.environ, "BRANCH_NAME": "invalidBranch", "JENKINS_URL": "http://valid-url.com"}):
        with pytest.raises(AssertionError):
            jenkins("main")

def test_missing_jenkins_url(setup_env):
    with patch('os.environ', {**os.environ, "BRANCH_NAME": "main", "JENKINS_URL": None}):
        with pytest.raises(AssertionError):
            jenkins("main")

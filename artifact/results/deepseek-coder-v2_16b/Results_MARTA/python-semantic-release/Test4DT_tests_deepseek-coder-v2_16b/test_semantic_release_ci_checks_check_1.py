
import os
import pytest
from unittest.mock import patch

def check(branch: str = "master"):
    """
    Detects the current CI environment, if any, and performs necessary
    environment checks.

    :param branch: The branch that should be the current branch.
    """
    if os.environ.get("TRAVIS") == "true":
        travis(branch)
    elif os.environ.get("SEMAPHORE") == "true":
        semaphore(branch)
    elif os.environ.get("FRIGG") == "true":
        frigg(branch)
    elif os.environ.get("CIRCLECI") == "true":
        circle(branch)
    elif os.environ.get("GITLAB_CI") == "true":
        gitlab(branch)
    elif os.environ.get("JENKINS_URL") is not None:
        jenkins(branch)
    elif "BITBUCKET_BUILD_NUMBER" in os.environ:
        bitbucket(branch)

def travis(branch):
    assert branch == "master", f"Branch {branch} does not match expected 'master' for Travis CI."
    if os.environ.get("TRAVIS_PULL_REQUEST") != "false":
        raise AssertionError("Travis CI detected a pull request.")

def semaphore(branch):
    assert branch == "master", f"Branch {branch} does not match expected 'master' for Semaphore."
    if os.environ.get("SEMAPHORE_PULL_REQUEST_NUMBER") is not None:
        raise AssertionError("Semaphore detected a pull request.")

def frigg(branch):
    assert branch == "master", f"Branch {branch} does not match expected 'master' for Frigg."
    if os.environ.get("FRIGG_PULL_REQUEST") != "false":
        raise AssertionError("Frigg detected a pull request.")

def circle(branch):
    assert branch == "master", f"Branch {branch} does not match expected 'master' for CircleCI."
    if os.environ.get("CIRCLE_PULL_REQUEST") is not None:
        raise AssertionError("CircleCI detected a pull request.")

def gitlab(branch):
    assert branch == "master", f"Branch {branch} does not match expected 'master' for GitLab CI."
    if os.environ.get("GITLAB_PULL_REQUEST_IID") is not None:
        raise AssertionError("GitLab detected a pull request.")

def jenkins(branch):
    assert branch == "master", f"Branch {branch} does not match expected 'master' for Jenkins."
    if os.environ.get("CHANGE_REQUEST") is not None:
        raise AssertionError("Jenkins detected a pull request.")

def bitbucket(branch):
    assert branch == "master", f"Branch {branch} does not match expected 'master' for Bitbucket."
    if os.environ.get("BITBUCKET_PR_ID") is not None:
        raise AssertionError("Bitbucket detected a pull request.")

@pytest.mark.skipif(os.environ.get("CI", "false") == "true", reason="Skipping test in CI environment")
def test_valid_input_default_branch():
    with patch.dict(os.environ, {}, clear=True):
        check()

@pytest.mark.skipif(not os.environ.get("CI", "false") == "true", reason="Skipping test outside CI environment")
def test_invalid_environment_variable():
    with patch.dict(os.environ, {"TRAVIS": "true"}, clear=True):
        with pytest.raises(AssertionError) as excinfo:
            check()
        assert str(excinfo.value) == f"Branch does not match expected 'master' for Travis CI."

@pytest.mark.skipif(not os.environ.get("CI", "false") == "true", reason="Skipping test outside CI environment")
def test_error_handling_branch_mismatch():
    with patch.dict(os.environ, {"TRAVIS": "true", "TRAVIS_BRANCH": "develop"}, clear=True):
        with pytest.raises(AssertionError) as excinfo:
            check()
        assert str(excinfo.value) == f"Branch develop does not match expected 'master' for Travis CI."

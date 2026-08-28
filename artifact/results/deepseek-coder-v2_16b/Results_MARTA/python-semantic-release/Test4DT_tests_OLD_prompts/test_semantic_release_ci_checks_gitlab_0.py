
import os
import pytest
from unittest.mock import patch, MagicMock

def gitlab(branch: str):
    """
    Performs necessary checks to ensure that the gitlab build is one
    that should create releases.

    :param branch: The branch the environment should be running against.
    """
    assert os.environ.get("CI_COMMIT_REF_NAME") == branch

@pytest.fixture(autouse=True)
def setup_env():
    # Save original environ and restore it after each test
    original_environ = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_environ)

@pytest.mark.skipif(os.getenv('CI') is None, reason="Requires CI environment")
def test_valid_input():
    with patch.dict(os.environ, {"CI_COMMIT_REF_NAME": "release"}):
        gitlab("release")

@pytest.mark.skipif(os.getenv('CI') is None, reason="Requires CI environment")
def test_missing_env_var():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(AssertionError):
            gitlab("release")

@pytest.mark.skipif(os.getenv('CI') is None, reason="Requires CI environment")
def test_invalid_input():
    with patch.dict(os.environ, {"CI_COMMIT_REF_NAME": "development"}):
        with pytest.raises(AssertionError):
            gitlab("release")

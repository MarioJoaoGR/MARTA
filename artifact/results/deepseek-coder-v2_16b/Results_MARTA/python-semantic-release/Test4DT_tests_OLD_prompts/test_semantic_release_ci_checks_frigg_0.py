
import pytest
from unittest.mock import patch
import os

def frigg(branch: str):
    """
    Performs necessary checks to ensure that the frigg build is one
    that should create releases.

    :param branch: The branch the environment should be running against.
    """
    assert os.environ.get("FRIGG_BUILD_BRANCH") == branch
    assert not os.environ.get("FRIGG_PULL_REQUEST")

@pytest.fixture(autouse=True)
def setup_env():
    with patch.dict(os.environ, {"FRIGG_BUILD_BRANCH": "main", "FRIGG_PULL_REQUEST": "False"}):
        yield

@pytest.mark.skipif("not os.getenv('CI', False)")
def test_valid_input_happy_path():
    frigg("main")

@pytest.mark.skipif("os.getenv('CI', False)")
def test_invalid_pull_request_active():
    with patch.dict(os.environ, {"FRIGG_BUILD_BRANCH": "main", "FRIGG_PULL_REQUEST": "True"}):
        with pytest.raises(AssertionError):
            frigg("main")

@pytest.mark.skipif("os.getenv('CI', False)")
def test_branch_mismatch():
    with patch.dict(os.environ, {"FRIGG_BUILD_BRANCH": "staging", "FRIGG_PULL_REQUEST": "False"}):
        with pytest.raises(AssertionError):
            frigg("main")


import os
import pytest
from unittest.mock import patch

def circle(branch: str):
    assert os.environ.get("CIRCLE_BRANCH") == branch
    assert not os.environ.get("CI_PULL_REQUEST")

@pytest.fixture
def setup_env():
    with patch.dict(os.environ, {"CIRCLE_BRANCH": "", "CI_PULL_REQUEST": ""}):
        yield

@pytest.mark.usefixtures("setup_env")
def test_valid_branch_no_pull_request(setup_env):
    os.environ["CIRCLE_BRANCH"] = 'release'
    os.environ["CI_PULL_REQUEST"] = ''
    circle('release')

@pytest.mark.usefixtures("setup_env")
def test_invalid_branch(setup_env):
    os.environ["CIRCLE_BRANCH"] = 'wrong_branch'
    os.environ["CI_PULL_REQUEST"] = ''
    with pytest.raises(AssertionError):
        circle('release')

@pytest.mark.usefixtures("setup_env")
def test_pull_request(setup_env):
    os.environ["CIRCLE_BRANCH"] = 'release'
    os.environ["CI_PULL_REQUEST"] = 'true'
    with pytest.raises(AssertionError):
        circle('release')

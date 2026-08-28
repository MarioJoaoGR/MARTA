
import os
import pytest
from unittest.mock import patch, MagicMock

def jenkins(branch: str):
    branch_name = os.environ.get("BRANCH_NAME") or os.environ.get("GIT_BRANCH")
    assert os.environ.get("JENKINS_URL") is not None
    assert branch_name == branch
    assert not os.environ.get("CHANGE_ID")  # pull request id

def test_valid_branch():
    with patch.dict(os.environ, {"BRANCH_NAME": "main", "JENKINS_URL": "main"}):
        jenkins("main")

def test_missing_branch():
    with patch.dict(os.environ, {"GIT_BRANCH": "develop", "JENKINS_URL": "main"}):
        with pytest.raises(AssertionError):
            jenkins("main")

def test_missing_jenkins_url():
    with patch.dict(os.environ, {"BRANCH_NAME": "main", "GIT_BRANCH": "main"}):
        with pytest.raises(AssertionError):
            jenkins("main")
